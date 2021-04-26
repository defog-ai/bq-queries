import psycopg2

create_overall = """CREATE TABLE IF NOT EXISTS overall (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  device_type TEXT,
  users BIGINT,
  sessions BIGINT,
  pageviews BIGINT,
  pageviews_w_timespent BIGINT,
  tot_time BIGINT,
  pageviews_w_affluence BIGINT,
  affluence_index BIGINT,
  search_pageviews BIGINT,
  social_pageviews BIGINT,
  forum_pageviews BIGINT,
  direct_pageviews BIGINT,
  other_pageviews BIGINT,
  first_pageviews BIGINT,
  first_sessions BIGINT,
  pageviews_active_last_day BIGINT,
  pageviews_active_last_week BIGINT
);"""

create_url = """CREATE TABLE IF NOT EXISTS url (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  users BIGINT,
  sessions BIGINT,
  pageviews BIGINT,
  pageviews_w_timespent BIGINT,
  tot_time BIGINT,
  pageviews_w_affluence BIGINT,
  affluence_index BIGINT,
  first_pageviews BIGINT,
  first_session_pageviews BIGINT,
  pageviews_active_last_day BIGINT,
  pageviews_active_last_week BIGINT,
  pageviews_ts_lt_30 BIGINT,
  pageviews_ts_30_60 BIGINT,
  pageviews_ts_60_90 BIGINT,
  pageviews_ts_90_120 BIGINT,
  pageviews_ts_120_150 BIGINT,
  pageviews_ts_150_180 BIGINT,
  pageviews_ts_gt_180 BIGINT,
  pageviews_sd_lt_20 BIGINT,
  pageviews_sd_20_40 BIGINT,
  pageviews_sd_40_60 BIGINT,
  pageviews_sd_60_80 BIGINT,
  pageviews_sd_gt_80 BIGINT
);"""

create_geography = """CREATE TABLE IF NOT EXISTS geography (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  url_path TEXT,
  users BIGINT,
  sessions BIGINT,
  pageviews BIGINT,
  pageviews_w_timespent BIGINT,
  tot_time BIGINT,
  pageviews_w_affluence BIGINT,
  affluence_index BIGINT,
  first_pageviews BIGINT,
  first_sessions BIGINT,
  pageviews_active_last_day BIGINT,
  pageviews_active_last_week BIGINT
);"""

create_next_url = """CREATE TABLE IF NOT EXISTS next_url (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  session_referrer TEXT,
  device_type TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  from_url TEXT,
  to_url TEXT,
  pageviews BIGINT
);"""

create_event_1 = """CREATE TABLE IF NOT EXISTS event1 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_2 = """CREATE TABLE IF NOT EXISTS event2 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_3 = """CREATE TABLE IF NOT EXISTS event3 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_4 = """CREATE TABLE IF NOT EXISTS event4 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_5 = """CREATE TABLE IF NOT EXISTS event5 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_6 = """CREATE TABLE IF NOT EXISTS event6 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_7 = """CREATE TABLE IF NOT EXISTS event7 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_8 = """CREATE TABLE IF NOT EXISTS event8 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_9 = """CREATE TABLE IF NOT EXISTS event9 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

create_event_10 = """CREATE TABLE IF NOT EXISTS event10 (
  client_id TEXT NOT NULL,
  date INT,
  hour INT,
  url_path TEXT,
  device_type TEXT,
  session_referrer TEXT,
  country TEXT,
  province TEXT,
  city TEXT,
  event TEXT,
  hits BIGINT
);"""

conn = psycopg2.connect(host="localhost", dbname="fsd_analytics", user="postgres", password="")
cur = conn.cursor()
cur.execute(create_overall)
cur.execute(create_url)
cur.execute(create_geography)
cur.execute(create_next_url)
cur.execute(create_event_1)
cur.execute(create_event_2)
cur.execute(create_event_3)
cur.execute(create_event_4)
cur.execute(create_event_5)
cur.execute(create_event_6)
cur.execute(create_event_7)
cur.execute(create_event_8)
cur.execute(create_event_9)
cur.execute(create_event_10)
conn.commit()
cur.close()