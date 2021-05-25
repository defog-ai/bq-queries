SELECT
  client_id,
  CAST(EXTRACT(DATE from cur_time) AS STRING) date,
  CONCAT(CAST(EXTRACT(DATE from cur_time) AS STRING), "-", LPAD(CAST(EXTRACT(HOUR from cur_time) AS STRING), 2, '0')) hour,
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
  COUNT(CASE WHEN active_last_7days THEN 1 END) pageviews_active_last_week,
  COUNT(CASE WHEN time_spent BETWEEN 0 AND 30 THEN 1 END) pageviews_ts_lt_30,
  COUNT(CASE WHEN time_spent BETWEEN 30 AND 60 THEN 1 END) pageviews_ts_30_60,
  COUNT(CASE WHEN time_spent BETWEEN 60 AND 90 THEN 1 END) pageviews_ts_60_90,
  COUNT(CASE WHEN time_spent BETWEEN 90 AND 120 THEN 1 END) pageviews_ts_90_120,
  COUNT(CASE WHEN time_spent BETWEEN 120 AND 150 THEN 1 END) pageviews_ts_120_150,
  COUNT(CASE WHEN time_spent BETWEEN 150 AND 180 THEN 1 END) pageviews_ts_150_180,
  COUNT(CASE WHEN time_spent > 180 THEN 1 END) pageviews_ts_gt_180,
  COUNT(CASE WHEN max_depth BETWEEN 0 AND 20 THEN 1 END) pageviews_sd_lt_20,
  COUNT(CASE WHEN max_depth BETWEEN 20 AND 40 THEN 1 END) pageviews_sd_20_40,
  COUNT(CASE WHEN max_depth BETWEEN 40 AND 60 THEN 1 END) pageviews_sd_40_60,
  COUNT(CASE WHEN max_depth BETWEEN 60 AND 80 THEN 1 END) pageviews_sd_60_80,
  COUNT(CASE WHEN max_depth > 80 THEN 1 END) pageviews_sd_gt_80
FROM
  `the-broadline.fsd.web_ingestion`
WHERE
  (
    DATETIME(_PARTITIONTIME) >= "{from_time}" OR _PARTITIONTIME IS NULL
  )
GROUP BY
  client_id, date, hour, country, province, city, url_path, device_type, session_referrer
ORDER BY hour
;