from django.shortcuts import render, HttpResponse
from django.conf import settings
import requests
import json

# Create your views here.

def weather(request):
    if request.method == 'POST':
        data = request.POST
        city = data['city']
        base_url = f'http://api.weatherapi.com/v1/current.json?key={settings.API_KEY}&q={city}'
        try:
            fetch =  requests.get(base_url)
            to_dict = json.loads(fetch.content)
            status = fetch.status_code
            print(to_dict)
            parsed_data ={
                    'city' : to_dict['location']['name'],
                    'temp' : to_dict['current']['temp_c'],
                    'feelslike' : to_dict['current']['feelslike_c'],
                    'humidity' : to_dict['current']['humidity'],
                    'icon' : to_dict['current']['condition']['icon']
            }
            print(to_dict['current']['temp_c'])
            return render(request, 'home.html', {'data' : parsed_data, 'status': status})
    
        except Exception as e:
            print(e)
            return render(request, 'home.html', {'error' : e})
        
            
    else:
        return render(request, 'home.html', {})

    
    
    
    
