from django.shortcuts import render
import requests
import json

def home(request):
    response = requests.get("https://coronavirus-19-api.herokuapp.com/countries/kenya")
    datas = response.json() 
    return render(request, 'home.html', {
        'cases': datas['cases'],
        'deaths':datas["deaths"], 
        'recovered':datas["recovered"], 
        'active':datas["active"], 
        'todaycases':datas["todayCases"], 
        'todaydeaths':datas["todayDeaths"], 
        'critical' :datas["critical"], 
        'tests':datas["totalTests"]
        
        
        })

def index(request):
    response = requests.get("https://corona.lmao.ninja/v2/countries/kenya")
    data = response.json() 
    return render(request, 'index.html', {
        'cases': data['cases'],
        'deaths':data["deaths"], 
        'recovered':data["recovered"], 
        'active':data["active"], 
        'todaycases':data["todayCases"], 
        'todaydeaths':data["todayDeaths"],
        'todayrecovered':data["todayRecovered"], 
        'critical' :data["critical"], 
        'tests':data["tests"]
        
        
        })
    


