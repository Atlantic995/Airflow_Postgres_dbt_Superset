import psycopg2
# from api_request.api_request import mock_fetch_data
from api_request.api_request import fetch_data


def connect_to_db():
    print("Connecting to the PostgreSQL database ...")
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise
    

def create_table(conn):
    print("Creating table if it does not exist...")
    try:
        cursor = conn.cursor() # object that allows you to interact with the data base and execute queries
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                       id SERIAL PRIMARY KEY,
                       city TEXT,
                       temperature FLOAT,
                       weather_descriptions TEXT,
                       wind_speed FLOAT,
                       time TIMESTAMP,
                       inserted_at TIMESTAMP DEFAULT NOW(),
                       utc_offset TEXT
            );
        """)
        conn.commit()
        print("Table was created.")

    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        raise



def insert_records(conn, data):
    print("Trying to insert data to the data base")
    try:
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                inserted_at,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print("Data successfully inserted")
    except psycopg2.Error as e:
        print(f"An error has occured during data insertion : {e}")
        raise

def main():
    try:
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except psycopg2.Error as e:
        print(f"An error has occurred during execution: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("DB connection closed.")

