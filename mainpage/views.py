from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request -> response
#response handler

def say_hello(request):
    return render(request, 'home.html')
