from django.shortcuts import render
from WeatherForU import settings
import requests,json
from home.models import CityName
import geocoder
from datetime import date, datetime
from tzwhere import tzwhere
from pytz import timezone
from timezonefinder import TimezoneFinder
from  geopy.geocoders import Nominatim

# Create your views here.

def index(request):
    today = date.today().strftime("%d/%m/%Y")
    now = datetime.now().strftime("%H:%M:%S")
    cities = CityName.objects.all()
    return render(request, 'index.html', {'cities': cities, "date": today, "time": now})
        
def search(request):
    if request.method == 'POST':
        search = request.POST["search"]
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "q=" + search + "&appid=" + settings.api_key
        response = requests.get(complete_url) 
        x = response.json() 
        y = x["main"] 
        temp= round(int(y["temp"])-273.15,2)
        max_temp= round(int(y["temp_max"])-273.15,2)
        min_temp= round(int(y["temp_min"])-273.15,2)
        pressure = y["pressure"] 
        humidity = y["humidity"] 
        z = x["weather"] 
        a = x["wind"]
        wind = a["speed"]
        desc = z[0]["description"]
        icon = z[0]["icon"]
        place = x["name"]
        photo_key = settings.photo_key
        photo_api = "https://pixabay.com/api/?key="+ photo_key + "&q=" + place + "&image_type=photo"
        response = requests.get(photo_api) 
        p = response.json()
        p1 = p["hits"]
        name_photo = p1[0]["webformatURL"]
        geolocator = Nominatim(user_agent="WeatherForU")
        loc = geolocator.geocode(place)
        tf = TimezoneFinder()
        timezone = tf.timezone_at(lng=loc.longitude, lat=loc.latitude)
        url1 = "http://worldtimeapi.org/api/timezone/"
        complete_url1 = url1 + timezone
        response1 = requests.get(complete_url1) 
        x = response1.json()
        datetime = str(x["datetime"])
        date = datetime[0:10]
        time = datetime[11:18]
        context ={
            "temp": temp,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "pressure": pressure,
            "humidity": humidity,
            "desc": desc,
            "wind": wind,
            "icon": icon,
            "place": place,
            "name_photo": name_photo,
            "date": date,
            "time": time
        }
        return render(request, "search.html", context=context)

def present(request):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    g = geocoder.ip('me')
    lat = str(g.lat)
    lon = str(g.lng)
    complete_url = base_url + "lat=" + lat + "&lon="  + lon + "&appid=" + settings.api_key
    response = requests.get(complete_url) 
    x = response.json() 
    y = x["main"] 
    temp= round(int(y["temp"])-273.15,2)
    max_temp= round(int(y["temp_max"])-273.15,2)
    min_temp= round(int(y["temp_min"])-273.15,2)
    pressure = y["pressure"] 
    humidity = y["humidity"] 
    z = x["weather"] 
    a = x["wind"]
    wind = a["speed"]
    desc = z[0]["description"]
    icon = z[0]["icon"]
    name = x["name"]
    photo_key = settings.photo_key
    photo_api = "https://pixabay.com/api/?key="+ photo_key + "&q=" + name + "&image_type=photo"
    response = requests.get(photo_api) 
    p = response.json()
    p1 = p["hits"]
    name_photo = p1[0]["webformatURL"]
    today = date.today().strftime("%d/%m/%Y")
    now = datetime.now().strftime("%H:%M:%S")
    context ={
            "temp": temp,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "pressure": pressure,
            "humidity": humidity,
            "desc": desc,
            "wind": wind,
            "icon": icon,
            "name": name,
            "name_photo": name_photo,
            "time": now,
            "date": today
        }
    return render(request, "live.html", context=context)