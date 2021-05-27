import psycopg2
from google.cloud import bigquery
from datetime import datetime, timedelta
import os

#Setting up location of directory with SQL queries
sql_queries_path = "/home/rishabhsriv/bq-queries/sql_queries"

#Setting up Google Authentication
json_key = '/home/rishabhsriv/google_key.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key

def delete_from_postgres(query):
  conn = psycopg2.connect(host="localhost", dbname="fsd_analytics", user="postgres", password=os.environ["POSTGRES_PASSWORD"])
  cur = conn.cursor()
  cur.execute(query)
  conn.commit()
  cur.close()
  return True

def insert_to_postgres(table_name, data=(), num_cols=0):
  """
  `table_name` is a string
  `data` is a tuple of tuples
  """
  conn = psycopg2.connect(host="localhost", dbname="fsd_analytics", user="postgres", password=os.environ["POSTGRES_PASSWORD"])
  cur = conn.cursor()
  values_placeholder = ', '.join(['%s' for _ in range(num_cols)])
  cur.executemany(f"INSERT INTO {table_name} VALUES({values_placeholder})", data)
  conn.commit()
  cur.close()
  return True

def run_bq_query(query):
  client = bigquery.Client()
  query_job = client.query(query)  # Make an API request.
  rows = []
  for row in query_job:
      rows.append([row[i] for i in range(len(row))])
  return rows

#set the from_time and to_time to get the right partitions to query
from_time = (datetime.utcnow() - timedelta(hours=2)).strftime("%Y-%m-%d %H:00:00")

#delete duplicate rows in BigQuery
with open(f"{sql_queries_path}/delete_duplicates.sql", "r") as f:
  query = f.read()

query = query.format(from_time=from_time)
run_bq_query(query)

#delete data for the last hour on postgres
base_query = "DELETE FROM {table_name} WHERE hour >= {from_time}"

## first, for the non-event tables
table_names = ["overall", "geography", "next_url"]
for table in table_names:
  query_to_run = base_query.format(table_name=table, from_time=from_time)
  delete_from_postgres(query_to_run)

## then, for event tables
for num in range(1, 11):
  query_to_run = base_query.format(table_name=f"event{num}", from_time=from_time)
  delete_from_postgres(query_to_run)

#run queries to summarize bigquery data and put it into postgres (non-event)
queries_and_associated_tables = [
  {"query_fname": "get_overall.sql", "table_name": "overall", 'num_cols': 20},
  {"query_fname": "get_geography.sql", "table_name": "geography", 'num_cols': 32},
  {"query_fname": "next_url.sql", "table_name": "next_url", 'num_cols': 11}
]

for item in queries_and_associated_tables:
  with open(f"{sql_queries_path}/{item['query_fname']}", "r") as f:
    query = f.read()

  query = query.format(from_time=from_time)
  values = run_bq_query(query)
  insert_to_postgres(item['table_name'], values, num_cols=item['num_cols'])

#run queries to summarize bigquery data and put it into postgres (event)
for num in range(1,11):
  with open(f"{sql_queries_path}/get_events.sql", "r") as f:
    query = f.read()
  
  query = query.format(num=num, from_time=from_time)
  values = run_bq_query(query)
  insert_to_postgres(f"event{num}", values, num_cols=11)