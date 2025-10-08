
  
    

  create  table "db"."dev"."staging__dbt_tmp"
  
  
    as
  
  (
    

SELECT *
FROM "db"."dev"."raw_weather_data"
  );
  