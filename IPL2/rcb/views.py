from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain (request):
    return HttpResponse('<h1>Faf du Plessis</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Virat Kohli</h1>')