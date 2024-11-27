from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def RohitSharma(request):
    return HttpResponse('<h1>Rohit Sharma is the leading Batsman in MI..</h1>')