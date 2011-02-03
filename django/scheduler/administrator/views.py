from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response
from scheduler.algorithm.algotest import Algorithm
from django import forms

from scheduler.administrator.csv_import import csv_import

class csv_form(forms.Form):
	file  = forms.FileField()

def upload_csv(request):
	if request.method == 'POST':
		form = csv_form(request.POST, request.FILES)
		if form.is_valid():
			csv_import(request.FILES['file'])
			html = "<html><body>Upload successful</body></html>"
			return HttpResponse(html)
	else:
		form = csv_form()
	return render_to_response('admin/csv_form.html', {'form': form})

def home(request):
	return render_to_response('admin.html', RequestContext(request))
