from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Virat(request):
    return HttpResponse('<h1>Virat Kohli also know as "GOAT" has scored 80 centuries in International Cricket..</h1>')