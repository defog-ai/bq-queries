SELECT
  client_id,
  EXTRACT(DATE from cur_time) date,
  EXTRACT(HOUR from cur_time) hour,
  url_path,
  device_type,
  session_referrer,
  COUNT(DISTINCT(uuid)) users,
  COUNT(DISTINCT(session_id)) sessions,
  COUNT(page_id) pageviews,
  COUNT(time_spent) pageviews_w_timespent,
  SUM(time_spent) time_spent,
  COUNT(affluence_index) pageviews_w_affuence,
  SUM(affluence_index) affluence_index,
  COUNT(CASE WHEN first_ever_pageview THEN 1 END) first_pageviews,
  COUNT(CASE WHEN first_ever_session THEN 1 END) first_session_pageviews,
  COUNT(CASE WHEN active_last_24hrs THEN 1 END) pageviews_active_last_day,
  COUNT(CASE WHEN active_last_7days THEN 1 END) pageviews_active_last_week,
  COUNT(CASE WHEN time_spent BETWEEN 0 AND 30 THEN 1 END) pageviews_ts_lt_30,
  COUNT(CASE WHEN time_spent BETWEEN 30 AND 60 THEN 1 END) pageviews_ts_30_60,
  COUNT(CASE WHEN time_spent BETWEEN 60 AND 90 THEN 1 END) pageviews_ts_60_90,
  COUNT(CASE WHEN time_spent BETWEEN 90 AND 120 THEN 1 END) pageviews_ts_90_120,
  COUNT(CASE WHEN time_spent BETWEEN 120 AND 150 THEN 1 END) pageviews_ts_120_150,
  COUNT(CASE WHEN time_spent BETWEEN 150 AND 180 THEN 1 END) pageviews_ts_150_180,
  COUNT(CASE WHEN time_spent > 180 THEN 1 END) pageviews_ts_gt_180,
  COUNT(CASE WHEN scroll_deph BETWEEN 0 AND 20 THEN 1 END) pageviews_sd_lt_20,
  COUNT(CASE WHEN scroll_deph BETWEEN 20 AND 40 THEN 1 END) pageviews_sd_20_40,
  COUNT(CASE WHEN scroll_deph BETWEEN 40 AND 60 THEN 1 END) pageviews_sd_40_60,
  COUNT(CASE WHEN scroll_deph BETWEEN 60 AND 80 THEN 1 END) pageviews_sd_60_80,
  COUNT(CASE WHEN scroll_deph > 80 THEN 1 END) pageviews_sd_gt_80
FROM
  `the-broadline.fsd.web_ingestion`
WHERE
  DATETIME(_PARTITIONTIME) BETWEEN "YYYY-MM-DD HH:00:00" AND "YYYY-MM-DD HH:00:00"
GROUP BY
  client_id, date, hour, url_path, device_type, session_referrer
;