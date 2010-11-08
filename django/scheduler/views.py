# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')  

def login(request):
    return render_to_response('login.html')

def logout(request):
	"""
	Log users out and redirect them to the main page.
	"""
	logout(request)
	return HttpResponseRedirect('/')