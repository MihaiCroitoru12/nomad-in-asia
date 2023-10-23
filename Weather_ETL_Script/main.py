import requests
import datetime
import psycopg2

# Connecting to the PostgreSQL database
conn = psycopg2.connect(
    host="YOUR_HOST_HERE",
    database="YOUR_DATABASE_HERE",
    user="YOUR_USER_HERE",
    password="YOUR_PASSWORD_HERE")

# OpenWeatherMap API key and URL
cur = conn.cursor()

api_key = 'YOUR_API_KEY_HERE'
api_url = 'https://api.openweathermap.org/data/2.5/weather?'

# List of cities in Southeast Asia
cities = ["Bangkok,TH", "Hanoi,VN", "Jakarta,ID", "Kuala Lumpur,MY", "Manila,PH", "Singapore,SG", "Naypyidaw,MM", "Phnom Penh,KH", "Vientiane,LA", "Bandar Seri Begawan,BN", "Dili,TL"]

# SQL query template for inserting data into the database
insert_query = """
    INSERT INTO weather_data (
        country, city, temperature, humidity, pressure, wind_speed, description, recorded_at, local_time, temperature_alert, humidity_alert, wind_alert)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

# Looping through each city to fetch and store weather data
for city in cities:
     # Preparing parameters for the API request
    parameters = {'q':city, 'appid' : api_key, 'units': 'metric'}
    response = requests.get(api_url, params=parameters)
    data = response.json()

    # Extracting country and city name from the response
    country_city_splitted = city.split(',')
    country_splitted = country_city_splitted[1]
    city_splitted  =country_city_splitted[0]
    
    # Extracting weather data from the response
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Setting alert flags based on certain conditions
    temperature_alert = "Yes" if temperature > 35 else "No"
    humidity_alert = "Yes" if humidity > 85 else "No"  
    wind_alert = "Yes" if wind_speed > 20 else "No"  

    # More data extraction from the response
    pressure = data['main']['pressure']
    description = data['weather'][0]['description']
    recorded_at = datetime.datetime.now()
    local_time_unix = data['dt'] + data['timezone']
    local_time = (datetime.datetime.utcfromtimestamp(int(local_time_unix)).strftime('%Y-%m-%d %H:%M:%S'))


    # Inserting the extracted data into the PostgreSQL database
    cur.execute(insert_query, (
        country_splitted, city_splitted, temperature, humidity, pressure, wind_speed, description, recorded_at, local_time, temperature_alert, humidity_alert, wind_alert))
    print("Data inserted for: " + city)
# Committing the transaction
conn.commit()

# Closing the cursor and connection
cur.close()
conn.close()




 