from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse('<h1>Ruturaj is the Captain of CSK</h1>')