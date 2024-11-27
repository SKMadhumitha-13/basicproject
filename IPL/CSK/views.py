from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Dhoni(request):
    return HttpResponse('<h1>Captain MS Dhoni is yet to do the Batting..</h1>')