# WeatherForU Web App
<img src="static/img/officiallogo.png" style="height:px;50 width:100px;">

## Description
A website which gives info about a required city's weather or the weather updates of the current location of the user. Made using Django and some API's

This is an open source project. Feel free to open issues if you find any bug or want to add some feature.

[Download the App](https://adityaashvin.github.io/weatherforuweb.github.io/)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)
## Features of the website
>1. Gives weather updates for any major city in the world and also gives weather updates of the current location of the user.
>2. Weather updates include temperature, humidity, maximum temperature, minimum temperature, atmospheric pressure, and a basic description(such as "light drizzle", "mist", "cloudy" to name a few)
>3. The local time and date of the city searched is also displayed in the navbar.
## Steps to run this in yoour local machine
### 1. Clone the repo
> git clone https://github.com/AdityaAshvin/WeatherForU.git
### 2. Install python
> https://realpython.com/installing-python/
### 3. Install django
> https://docs.djangoproject.com/en/3.0/topics/install/
### 4. Install required addition dependencies
> Run the following command
>> pip install -r requirements.txt
### 5. Get Weather api
> [OpenWeather](https://openweathermap.org/)
### 6. Get Images api
> [Pixabay](https://pixabay.com/api/docs/)
### 7. Add the above mentioned api keys in the settings file inside "WeatherForU" directory
> ![ss](static/img/ss/api.JPG)
### Final step
> Run the following command
>> python manage.py runserver
# Screenshots
## Homepage
![homepage1](static/img/ss/home1.JPG)
## Current Location (which in my case is Visakhapatnam)
![current1](static/img/ss/current1.JPG)
![current2](static/img/ss/current2.JPG)
## When Delhi is searched
![search1](static/img/ss/search_delhi1.JPG)
![search2](static/img/ss/search_delhi2.JPG)
## When Chicago is searched
![search1](static/img/ss/search_chicago1.JPG)
![search2](static/img/ss/search_chicago2.JPG)

### API's used:
1 [OpenWeather](https://openweathermap.org/) - for live weather data
2 [Pixabay](https://pixabay.com) - for city images
