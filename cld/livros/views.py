from django.shortcuts import render
from django.http import HttpResponse

from . import urls

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're from the coins index")
