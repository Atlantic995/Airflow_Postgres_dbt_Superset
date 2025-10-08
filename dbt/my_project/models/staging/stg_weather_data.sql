{{ config(
    materialized='table',
    unqiue_key='id'
)}}

with source as (SELECT *
FROM {{ source('dev', 'raw_weather_data')}}),

de_dup AS (
    SELECT 
    *,
    row_number() OVER(PARTITION BY TIME ORDER BY inserted_at) AS rn
    FROM source
)


SELECT
    id,
    city,
    temperature,
    weather_descriptions,
    wind_speed,
    TIME AS weather_time_local,
    (inserted_at + (utc_offset || 'hours')::interval) AS inserted_at_local
FROM de_dup 
WHERE rn = 1
