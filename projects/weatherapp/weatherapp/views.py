from django.shortcuts import render
import requests
from decouple import config
from pprint import pprint
from .models import City

# Create your views here.

def index(request):
    cities = City.objects.all()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    #city = "Berlin"
    #response = requests.get(url.format(city, config ("API_KEY")))
    #content= response.json()
    #pprint(content)
    #print(type(content))

    u_city = request.GET.get("name")
    print("user_city: ", u_city)

    if u_city:
        response = requests.get(url.format(u_city, config("API_KEY")))
        print(response.status_code)
        if response.status_code == 200:
            content = response.json()
            r_city = content["name"]
            if City.objects.filter(name=r_city):
                messages.warning(request, "City already exists.")
            else:
                City.objects.create(name=r_city)
                messages.success(request, "City succesfully created.")
        else:
            messages.warning(request, "City not found.")
        return redirect("home")

    city_data = []
    for city in cities:
        #print(city)
        response = requests.get(url.format(city, config ("API_KEY")))
        content= response.json()
        #pprint(content)

        data = {
            "city": city,
            "temp": content["main"]["temp"],
            "desc": content["weather"][0]["description"],
            "icon": content["weather"][0]["icon"]
        }

        city_data.append(data)
        #pprint(city_data)
        context = {
            "city_data": city_data
        }

    return render(request, "weatherapp/index.html", context)