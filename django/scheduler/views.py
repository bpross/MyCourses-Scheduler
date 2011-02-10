# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

def index(request):
	if request.user.is_authenticated:
		if request.user.is_staff:
			if request.user.is_superuser: # Admin
				return HttpResponseRedirect('/administrator')
			else: # Manager
				return render_to_response('base.html', RequestContext(request))
		else: # Lecturer/Student
			return render_to_response('base.html', RequestContext(request))
	else: # Not logged in			
		return render_to_response('base.html', RequestContext(request))  
	


def login(request):
    return render_to_response('login.html', RequestContext(request))

def logout_page(request):
	"""
	Log users out and redirect them to the main page.
	"""
	logout(request)
	return HttpResponseRedirect('/')

def manual(request):
   return render_to_response('manual.html')
#
def placeholder(request):
    return render_to_response('placeholder.html', RequestContext(request))
    
#def error(request):
#	return http.HttpResponseServerError(a_template.render(RequestContext(request, {})))
#
#def shoppingcart(request):
#    return render_to_response('shoppingCart.html', RequestContext(request))
#
#def managecourses(request):
#    return render_to_response('courseManager.html', RequestContext(request))
#
#def settings(request):
#    return render_to_response('settings.html', RequestContext(request))
