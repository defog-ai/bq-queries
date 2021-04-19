-- TODO: add time constraints

SELECT
  t1.client_id,
  t1.url_path AS from_url,
  t2.url_path AS to_url,
  COUNT(t2.url_path) as pageviews
FROM (
  SELECT
    client_id,
    url_path,
    session_id,
    session_hit_num
  FROM
    `the-broadline.fsd.web_ingestion`
  WHERE
    DATETIME(_PARTITIONTIME) BETWEEN "YYYY-MM-DD HH:00:00" AND "YYYY-MM-DD HH:00:00"
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
    DATETIME(_PARTITIONTIME) BETWEEN "YYYY-MM-DD HH:00:00" AND "YYYY-MM-DD HH:00:00"
  ORDER BY
    session_id, session_hit_num
) AS t2
ON
  t1.session_id = t2.session_id AND t2.session_hit_num = t1.session_hit_num + 1 AND t1.url_path != t2.url_path
GROUP BY
  t1.client_id, from_url, to_url
;