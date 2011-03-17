from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response


def calendar(request):
	return render_to_response('calendar.html', RequestContext(request))
