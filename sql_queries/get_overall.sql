-- TODO: add time partition constraints

SELECT
  client_id,
  EXTRACT(DATE from cur_time) date,
  EXTRACT(HOUR from cur_time) hour,
  COUNT(DISTINCT(uuid)) users,
  COUNT(DISTINCT(session_id)) sessions,
  COUNT(page_id) pageviews,
  AVG(time_spent) avg_time,
  COUNT(CASE WHEN first_ever_session THEN 1 END) num_first_ever_sessions,
  COUNT(CASE WHEN session_referrer = 'Google' THEN 1 END) google_pageviews,
FROM
  `the-broadline.fsd.web_ingestion`
GROUP BY
  client_id, date, hour
;