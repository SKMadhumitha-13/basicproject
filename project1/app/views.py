from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def madhu(request):
    return HttpResponse('<h1>Maddie loves travelling...</h1>')
