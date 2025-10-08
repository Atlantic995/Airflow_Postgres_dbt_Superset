

SELECT
    city,
    DATE(weather_time_local) AS DATE,
    ROUND(AVG(temperature)::numeric,2) AS avg_temperature,
    ROUND(AVG(wind_speed)::numeric,2) AS avg_wind_speed
FROM "db"."dev"."stg_weather_data"
GROUP BY
    city,
    DATE(weather_time_local)
ORDER BY
    city,
    DATE(weather_time_local)