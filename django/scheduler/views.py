# Create your views here.
#from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><body>Hi!</body></html>")
    #return render_to_response('index.html')  
