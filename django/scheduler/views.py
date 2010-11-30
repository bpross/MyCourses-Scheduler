# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', RequestContext(request))  

def login(request):
    return render_to_response('login.html')

def logout_page(request):
	"""
	Log users out and redirect them to the main page.
	"""
	logout(request)
	return HttpResponseRedirect('/')

def placeholder(request):
    return render_to_response('placeholder.html')

def shoppingcart(request):
    return render_to_response('shoppingCart.html')

def managecourses(request):
    return render_to_response('courseManager.html')

def settings(request):
    return render_to_response('settings.html')
