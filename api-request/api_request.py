import requests
api_key = "3e2e70623b49dc5ada2feb4aba1cc892"
city = "Bucharest"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"


def fetch_data():
     print("Fetching weather data from Weather API...")
     try:
         response = requests.get(api_url)
         response.raise_for_status()
         print("API response received successfully.")
         return response.json()
    
     except requests.exceptions.RequestException as e:
         print(f"An error occurred: {e}")
         raise

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-09-28 11:29', 'localtime_epoch': 1759058940, 'utc_offset': '-4.0'}, 'current': {'observation_time': '03:29 PM', 'temperature': 22, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '06:50 AM', 'sunset': '06:42 PM', 'moonrise': '01:40 PM', 'moonset': '10:13 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 31}, 'air_quality': {'co': '473.6', 'no2': '20.165', 'o3': '136', 'so2': '17.39', 'pm2_5': '25.53', 'pm10': '25.9', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 9, 'wind_degree': 236, 'wind_dir': 'WSW', 'pressure': 1018, 'precip': 0, 'humidity': 71, 'cloudcover': 75, 'feelslike': 22, 'uv_index': 4, 'visibility': 16, 'is_day': 'yes'}}