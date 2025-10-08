
  
    

  create  table "db"."dev"."weather_report__dbt_tmp"
  
  
    as
  
  (
    

SELECT 
    city,
    temperature,
    weather_descriptions,
    wind_speed,
    weather_time_local  
FROM "db"."dev"."stg_weather_data"
  );
  