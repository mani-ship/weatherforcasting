
from django.shortcuts import render
from django.contrib import messages
import requests #pip install requests 
import datetime

def home(request):
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'coimbatore'     
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=cb52cd82e59d21dbf0f1145ff29b30f3'
    PARAMS = {'units':'metric'}
    API_KEY =  'AIzaSyAhG5hPODErqjsmED_DcVXv4J81JKax4ao'
    SEARCH_ENGINE_ID = '12e1247af00f046f8'
    query = city + " 1920x1080"
    start = 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
    data = requests.get(city_url).json()
    search_items = data.get("items")
    image_url = search_items[1]['link']
    
    try:
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()
          return render(request,'index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          day = datetime.date.today()
          return render(request,'index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'coimbatore' , 'exception_occurred':exception_occurred,'image_url':image_url } )
               
    