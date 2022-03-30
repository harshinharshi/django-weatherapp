from django.shortcuts import render
import requests
from pprint import pprint
import datetime

# Create your views here.

def index(request):
    if 'city' in request.POST:
        city = request.POST['city'] 
    else:
        city = "kannur"
        #print(city)
    appid ='f1296ee3bcd982ac05116bc9538a2444'
    URL = 'https://api.openweathermap.org/data/2.5/weather'

    parameters = {'q':city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url = URL, params = parameters, )
    res = r.json()
    #pprint(res)
    #description = icon = temp_max = temp_min = ""
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp_max = res['main']['temp_max']
    temp_min = res['main']['temp_min']
    day = datetime.date.today()
    #print("\n",description)
    return render(request, 'WeatherData\index.html',{"description": description,
                                                     'icon':icon,
                                                     'temp_max': temp_max,
                                                     'temp_min': temp_min,
                                                     'day': day,
                                                     'city':city,
    })
