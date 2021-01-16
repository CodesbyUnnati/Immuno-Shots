from django.shortcuts import render,HttpResponse
import requests
# Create your views here.

def index(request):
    # API to get the data 
    URL = "https://corona.lmao.ninja/v2/countries/India"

    # sending get request and saving the response as response object 
    r = requests.get(url = URL)  

    liveData = r.json()

    data = {}
    data["population"] = f'{liveData["population"]:,}'
    data["totalCases"] = f'{liveData["cases"]:,}'
    data["totalRecovered"] = f'{liveData["recovered"]:,}'
    data["totalDeaths"] = f'{liveData["deaths"]:,}'
    print(data)
    return render(request,'index.html',data)

def hospital_data(request):
    return render(request, 'hospital_data.html')


def booking(request):
    return render (request, 'booking.html')


def appointment(request):
    return render (request, 'appointment.html')
