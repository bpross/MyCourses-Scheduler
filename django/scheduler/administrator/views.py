from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response
from scheduler.algorithm.algotest import Algorithm
from django import forms
from csv_import import CSV

class csv_form(forms.Form):
	file  = forms.FileField(required=True)
	type  = forms.TypedChoiceField(required=True,
				choices=(("professor", "Professor"),
						 ("department", "Department"),
						 ("school", "School"),
						 ("building", "Building"),
						 ("room", "Room"),
						 ("course", "Course"),
						 ("course_class", "Course Class"),
						 ("period", "Period"),
						 ),
				widget=forms.RadioSelect
				)

def upload_csv(request):
	if request.method == 'POST':
		form = csv_form(request.POST, request.FILES)
		if form.is_valid():
			myCSV = CSV()
			myCSV.csv_import(request.FILES['file'])
			html = "<html><body>Upload successful</body></html>"
			return HttpResponse(html)
	else:
		form = csv_form()
	return render_to_response('admin/csv_form.html', {'form': form}, RequestContext(request))

def home(request):
	return render_to_response('admin/admin.html', RequestContext(request))
