SELECT 
    c.country_name,
    p.year,
    MAX(p.population_density) AS population_density,
    ROUND(AVG(w.access_to_clean_water_percent)::numeric, 2) AS avg_clean_water_access
FROM 
    population_density p
JOIN 
    water_sources w ON p.country_id = w.country_id AND p.year = w.year
JOIN 
    country c ON p.country_id = c.country_id
WHERE 
    w.access_to_clean_water_percent < 60
GROUP BY 
    c.country_name, p.year
ORDER BY 
    c.country_name ASC, p.year ASC;










