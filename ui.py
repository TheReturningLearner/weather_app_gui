from tkinter import Tk, StringVar, Entry, Button, Label, messagebox
from weather_info import get_weather
from PIL import Image, ImageTk
from collections import namedtuple

app = Tk()
app.title("Weather App")
app.geometry("800x500")

photo = ImageTk.PhotoImage(Image.new("RGBA", (1,1)))
weather_image = Label(app, image=photo)

# entry where user can search for city
city_txt = StringVar()

# entry where user can search for country
country_txt = StringVar()


city_entry = Entry(app, textvariable=city_txt) #app is the params
city_entry.pack() # place window on screen

country_entry = Entry(app, textvariable=country_txt) #app is the params
country_entry.pack() # place window on screen

weather_tuple = namedtuple("Weather",["city", "country", "temperature_celsius", "temperature_fahrenheit", "icon", "weather"])

def extract_weather_data(city, country):
    weather_data = get_weather(city, country)
    if weather_data:
        return weather_tuple(*weather_data) # means that you are mapping weather data to the tuple

def create_image_icons(image_name): # created func that takes a param
    image_path = Image.open(image_name) # using PIL with .open and store param
    return ImageTk.PhotoImage(image_path) # PIL return Photoimage to display

def search(): 
    city = city_txt.get()
    country = country_txt.get()
    weather = extract_weather_data(city, country)

    if weather:
        location_city["text"] = weather.city
        location_country["text"] = weather.country
        temp_image['text'] = f'{weather.temperature_celsius:.2f}°C, {weather.temperature_fahrenheit:.2f}°F'
        weather_label['text'] = weather.weather
        photo = create_image_icons(f"weather_icons/{weather.icon}.png")
        weather_image.configure(image=photo)
        weather_image.image = photo
    else:
        messagebox.showerror("Error", f"Enable to locate city {city}. Please try again.")


# to create a button
search_button = Button(app, text="search", width=12, command=search) # you must make a function for the search var to be active.
search_button.pack()

# location label for city and country
location_city = Label(app, text="", font=("bold", 20))
location_city.pack()

# location label for country
location_country = Label(app, text="", font=("bold", 20))
location_country.pack()

# Image that corresponds with weather conditions.
weather_image.pack()

# Image for tempurature
temp_image = Label(app, text="")
temp_image.pack()

# weather label
weather_label = Label(app, text="")
weather_label.pack()

app.mainloop()