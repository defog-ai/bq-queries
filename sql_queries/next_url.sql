SELECT
  t1.client_id AS client_id,
  t1.date AS date,
  t1.hour AS hour,
  t1.session_referrer AS session_referrer,
  t1.device_type AS device_type,
  t1.country AS country,
  t1.province AS province,
  t1.city AS city,
  t1.url_path AS from_url,
  t2.url_path AS to_url,
  COUNT(t2.url_path) as pageviews
FROM (
  SELECT
    client_id,
    CAST(EXTRACT(DATE from cur_time) AS STRING) date,
    CAST(EXTRACT(HOUR from cur_time) AS STRING) hour,
    url_path,
    session_referrer,
    device_type,
    country,
    province,
    city,
    session_id,
    session_hit_num
  FROM
    `the-broadline.fsd.web_ingestion`
  WHERE
    DATETIME(_PARTITIONTIME) BETWEEN "{from_time}" AND "{to_time}"
  ORDER BY
    session_id, session_hit_num
) AS t1
INNER JOIN (
  SELECT
    url_path,
    session_id,
    session_hit_num
  FROM
    `the-broadline.fsd.web_ingestion`
  WHERE
    DATETIME(_PARTITIONTIME) BETWEEN "{from_time}" AND "{to_time}"
  ORDER BY
    session_id, session_hit_num
) AS t2
ON
  t1.session_id = t2.session_id AND t2.session_hit_num = t1.session_hit_num + 1 AND t1.url_path != t2.url_path
GROUP BY
  client_id, date, hour, session_referrer, device_type, country, province, city, from_url, to_url
;