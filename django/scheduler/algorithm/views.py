from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from scheduler.algorithm.algotest import Algorithm


def algorithm(request):
    if request.user.is_staff:
       Algorithm()
    return render_to_response('algorithm.html', RequestContext(request))