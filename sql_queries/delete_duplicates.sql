DELETE FROM
  `the-broadline.fsd.web_ingestion`
WHERE
  STRUCT(page_id, cur_time) NOT IN (
    SELECT AS STRUCT page_id, MAX(cur_time) cur_time 
    FROM `the-broadline.fsd.web_ingestion` 
    GROUP BY page_id
  )
  AND DATETIME(_PARTITIONTIME) BETWEEN "{from_time}" AND "{to_time}"
;