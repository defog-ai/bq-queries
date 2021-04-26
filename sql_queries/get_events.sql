-- Different query for each of event number

SELECT
  client_id,
  date,
  hour,
  url_path,
  device_type,
  session_referrer,
  country,
  province,
  city,
  event,
  COUNT(1) hits
FROM (
  SELECT
    client_id,
    CAST(EXTRACT(DATE from cur_time) AS STRING) date,
    CAST(EXTRACT(HOUR from cur_time) AS STRING) hour,
    device_type,
    session_referrer,
    session_id,
    url_path,
    country,
    province,
    city,
    SPLIT(event{num}_values, "||") event{num}_values
  FROM `the-broadline.fsd.web_ingestion`
  WHERE DATETIME(_PARTITIONTIME) BETWEEN "{from_time}" AND "{to_time}"
) t1
CROSS JOIN UNNEST(t1.event{num}_values) AS event
GROUP BY client_id, date, hour, url_path, device_type, session_referrer, country, province, city, event;