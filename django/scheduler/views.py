# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')  

def login(request):
    return render_to_response('login.html')
