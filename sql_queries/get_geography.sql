-- TODO: add time partitions. Join with lat-long coordinates

SELECT
  client_id,
  EXTRACT(DATE from cur_time) date,
  EXTRACT(HOUR from cur_time) hour,
  device_type,
  session_referrer,
  country,
  province,
  city,
  url_path,
  COUNT(DISTINCT(uuid)) users,
  COUNT(DISTINCT(session_id)) sessions,
  COUNT(page_id) pageviews,
  COUNT(time_spent) pageviews_w_timespent,
  SUM(time_spent) time_spent,
  COUNT(affluence_index) pageviews_w_affuence,
  SUM(affluence_index) affluence_index,
  COUNT(CASE WHEN first_ever_pageview THEN 1 END) first_pageviews,
  COUNT(DISTINCT(CASE WHEN first_ever_session THEN session_id END)) first_sessions,
  COUNT(CASE WHEN active_last_24hrs THEN 1 END) pageviews_active_last_day,
  COUNT(CASE WHEN active_last_7days THEN 1 END) pageviews_active_last_week
FROM
  `the-broadline.fsd.web_ingestion`
GROUP BY
  ROLLUP(client_id, date, hour, device_type, session_referrer, url_path, country, province, city)
;