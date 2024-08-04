import requests
from configparser import ConfigParser


url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# ConfigParser used to read the config.ini file where API key is stored
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']["API_key"]


def get_weather(city, country):
    result = requests.get(url.format(f"{city}, {country}", api_key))  
    print(result)
    if result:
        json = result.json()
        # To return a tuple that will return (city, country, temp_celc, temp_fahren, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temperature_kelvin = json['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon'] # you must add the first index if you recieve a TypeError  
        weather = json['weather'][0]['main']  # you must add the first index if you recieve a TypeError  
        total_info = (city, country, temperature_celsius, temperature_fahrenheit, icon, weather)
        return total_info
    else:
        return None
    

if __name__ == "__main__":
    print(get_weather('Paris', 'France'))
