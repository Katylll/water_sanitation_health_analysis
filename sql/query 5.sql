CREATE VIEW average_yoy_change_by_water_source_type AS
WITH yoy_changes AS (
    SELECT 
        c.country_name,
        w.year,
        w.water_source_type,
        (w.access_to_clean_water_percent - 
         LAG(w.access_to_clean_water_percent) OVER (
             PARTITION BY c.country_name, w.water_source_type 
             ORDER BY w.year
         ))::numeric AS raw_yoy_change
    FROM 
        water_sources w
    JOIN 
        country c ON w.country_id = c.country_id
)

SELECT 
    country_name,
    year,
    water_source_type,
    ROUND(AVG(raw_yoy_change), 2) AS avg_yoy_change
FROM 
    yoy_changes
GROUP BY 
    country_name, year, water_source_type
ORDER BY 
    country_name ASC, year ASC, water_source_type ASC;






