from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response
from scheduler.algorithm.algotest import Algorithm

def home(request):
	return render_to_response('admin.html', RequestContext(request))