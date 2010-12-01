# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from scheduler.algorithm.algotest import Algorithm

def index(request):
    return render_to_response('base.html', RequestContext(request))  

def login(request):
    return render_to_response('login.html')

def algorithm(request):
    if request.user.is_staff:
       Algorithm()
    return render_to_response('algorithm.html', RequestContext(request))

def logout_page(request):
	"""
	Log users out and redirect them to the main page.
	"""
	logout(request)
	return HttpResponseRedirect('/')

def placeholder(request):
    return render_to_response('placeholder.html', RequestContext(request))

def shoppingcart(request):
    return render_to_response('shoppingCart.html', RequestContext(request))

def managecourses(request):
    return render_to_response('courseManager.html', RequestContext(request))

#def settings(request):
#    return render_to_response('settings.html', RequestContext(request))
