SELECT 
    c.country_name,
    m.year,
    ROUND(AVG(m.turbidity)::numeric, 2) AS avg_turbidity,
    ROUND(AVG(m.ph_level)::numeric, 2) AS avg_ph,
    ROUND(AVG(m.dissolved_oxygen)::numeric, 2) AS avg_dissolved_oxygen,
    ROUND(AVG(s.sanitation_coverage)::numeric, 2) AS avg_sanitation_coverage,
    ROUND(AVG(s.healthcare_access_index)::numeric, 2) AS avg_healthcare_access,

    --Risk Score Calculation
    ROUND((
        AVG(m.turbidity)::numeric +                               -- pollution
        ABS(AVG(m.ph_level)::numeric - 7.0) +                     -- pH deviation
        (10 - AVG(m.dissolved_oxygen)::numeric) +                 -- oxygen deficiency
        (100 - AVG(s.sanitation_coverage)::numeric) / 10 +        -- low sanitation
        (100 - AVG(s.healthcare_access_index)::numeric) / 10      -- weak healthcare
    )::numeric, 2) AS risk_score

FROM 
    measurements m
JOIN 
    socio_economic_indicators s ON m.country_id = s.country_id AND m.year = s.year
JOIN 
    country c ON m.country_id = c.country_id
GROUP BY 
    c.country_name, m.year
ORDER BY 
    c.country_name ASC, m.year ASC;  -- highest risk countries at the top


