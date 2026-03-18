SELECT 
    c.country_name,
    s.year,
    ROUND(AVG(DISTINCT s.gdp_per_capita)::numeric, 2) AS avg_gdp_per_capita,
    ROUND(AVG(w.access_to_clean_water_percent)::numeric, 2) AS access_to_clean_water_percent
FROM 
    socio_economic_indicators s
JOIN 
    water_sources w ON s.country_id = w.country_id AND s.year = w.year
JOIN 
    country c ON s.country_id = c.country_id
GROUP BY 
    c.country_name, s.year
ORDER BY 
    c.country_name, s.year;


