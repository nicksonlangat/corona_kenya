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
    