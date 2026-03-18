CREATE OR REPLACE VIEW treatment_effectiveness_summary AS
WITH base_data AS (
    SELECT 
        c.country_name,
        w.year,
        w.water_source_type,
        w.water_treatment,
        ROUND(AVG(m.bacterial_count)::numeric, 2) AS avg_bacterial_count,
        ROUND(AVG(w.access_to_clean_water_percent)::numeric, 2) AS avg_clean_water_access,
        COUNT(*) AS sample_count
    FROM 
        water_sources w
    JOIN 
        country c ON w.country_id = c.country_id
    JOIN 
        measurements m ON w.country_id = m.country_id AND w.year = m.year
    WHERE 
        m.bacterial_count IS NOT NULL
        AND w.access_to_clean_water_percent IS NOT NULL
        AND w.water_treatment IS NOT NULL
    GROUP BY 
        c.country_name, w.year, w.water_source_type, w.water_treatment
),
scored AS (
    SELECT 
        country_name,
        year,
        water_source_type,
        water_treatment,
        avg_bacterial_count,
        avg_clean_water_access,
        sample_count,
        ROUND((100 - avg_bacterial_count / 100) + avg_clean_water_access, 2) AS effectiveness_score
    FROM base_data
),
flagged AS (
    SELECT 
        country_name,
        year,
        water_source_type,
        water_treatment,
        avg_bacterial_count,
        avg_clean_water_access,
        sample_count,
        effectiveness_score,
        ROUND(
            effectiveness_score -
            LAG(effectiveness_score) OVER (
                PARTITION BY country_name, water_source_type, water_treatment
                ORDER BY year
            ), 2
        ) AS score_change
    FROM scored
)
SELECT 
    country_name,
    year,
    water_source_type,
    water_treatment,
    avg_bacterial_count,
    avg_clean_water_access,
    sample_count,
    effectiveness_score,
    CASE 
        WHEN score_change IS NULL THEN 'N/A'
        WHEN score_change > 1 THEN 'Improving'
        WHEN score_change < -1 THEN 'Worsening'
        ELSE 'Stable'
    END AS trend_flag
FROM flagged
ORDER BY 
    country_name, water_source_type, water_treatment, year;