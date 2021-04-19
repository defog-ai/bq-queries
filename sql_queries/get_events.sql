-- Different query for each of event number

SELECT
  url_path,
  event1,
  COUNT(1) hits
FROM (
  SELECT
    client_id,
    EXTRACT(DATE from cur_time) date,
    EXTRACT(HOUR from cur_time) hour,
    device_type,
    session_referrer,
    uuid,
    session_id,
    url_path,
    country,
    province,
    city
    SPLIT(event1_values, "||") event1_values
  FROM `the-broadline.fsd.web_ingestion`
  WHERE DATETIME(_PARTITIONTIME) BETWEEN "YYYY-MM-DD HH:00:00" AND "YYYY-MM-DD HH:00:00"
) t1
CROSS JOIN UNNEST(t1.event1_values) AS event1
GROUP BY unroll(client_id, date, hour, url_path, event1)
ORDER BY hits DESC;