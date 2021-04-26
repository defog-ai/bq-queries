import psycopg2
from google.cloud import bigquery
from datetime import datetime, timedelta
import os

#Setting up location of directory with SQL queries
sql_queries_path = "/home/rishabhsriv/bq-queries/sql_queries"

#Setting up Google Authentication
json_key = '/home/rishabhsriv/google_key.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key

def insert_to_postgres(table_name, data=()):
  """
  `table_name` is a string
  `data` is a tuple of tuples
  """
  conn = psycopg2.connect(host="localhost", dbname="fsd_analytics", user="postgres", password="")
  cur = conn.cursor()
  values_placeholder = {', '.join(['%s' for _ in range(len(data[0]))])}
  cur.executemany(f"INSERT INTO {table_name} VALUES({values_placeholder})", data)
  conn.commit()
  cur.close()
  return True

def run_bq_query(query):
  client = bigquery.Client()
  query_job = client.query(query)  # Make an API request.
  rows = []
  for row in query_job:
      # Row values can be accessed by either field name or index.
      rows.append((row[i] for i in range(len(row))))
  return rows

#set the from_time and to_time to get the right partitions to query
from_time = (datetime.utcnow() - timedelta(hours=1)).strftime("%Y-%m-%d %H:00:00")
to_time = (datetime.utcnow() - timedelta(hours=0)).strftime("%Y-%m-%d %H:00:00")

#delete duplicate rows in the latest hour
with open(f"{sql_queries_path}/delete_duplicates.sql", "r") as f:
  query = f.read()

query = query.format(from_time=None, to_time=None)
run_bq_query(query)

queries_and_associated_tables = [
  {"query_fname": "get_overall.sql", "table_name": "overall"},
  {"query_fname": "get_url.sql", "table_name": "url"},
  {"query_fname": "get_geography.sql", "table_name": "geography"},
  {"query_fname": "next_url.sql", "table_name": "next_url"}
]

for item in queries_and_associated_tables:
  with open(f"{sql_queries_path}/{item['query_fname']}", "r") as f:
    query = f.read()

  query = query.format(from_time=None, to_time=None)
  values = run_bq_query(query)
  insert_to_postgres(item['table_name'], values)