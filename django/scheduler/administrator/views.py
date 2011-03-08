from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from csv_import import CSV

class csv_form(forms.Form):
	file  = forms.FileField(required=True)
	type  = forms.TypedChoiceField(required=True,
				choices=(("business", "Business"),
						 ("building", "Building"),
						 ("employer", "Employer"),
						 ("employee", "Employee"),
						 ),
				widget=forms.RadioSelect
				)

def upload_csv(request):
	if request.method == 'POST':
		form = csv_form(request.POST, request.FILES)
		if form.is_valid():
			myCSV = CSV()
			print "File type selected: %s" %(request.POST['type'])
			result = myCSV.csv_import(request.FILES['file'], request.POST['type'])
			if result:
				flag = "successful"
			else:
				flag = "failed"
			html = "<html><body>Upload %s.</body></html>" % (flag)
			return HttpResponse(html)
	else:
		form = csv_form()
	return render_to_response('admin/csv_form.html', {'form': form}, RequestContext(request))

def home(request):
	return render_to_response('admin/admin.html', RequestContext(request))

def calendar(request):
	return render_to_response('calendar.html', RequestContext(request))