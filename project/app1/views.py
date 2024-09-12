from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('''<h1 style="background-color: aqua">Welcome to Welcome</h1>  ''')

def home1(request):
    return HttpResponse('''Welcome to Welcome  ''')