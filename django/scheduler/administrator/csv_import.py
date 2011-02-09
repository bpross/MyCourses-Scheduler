import csv
file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/test")
testReader = csv.reader(file,deliminiter = ' ', quotechar = '|')
for row in testReader
    print "|".join(row)





def csv_import(f):
	for chunk in f.chunks():
		pass

	# Parse the imported CSV file here
	# Reference: http://docs.djangoproject.com/en/1.2/topics/http/file-uploads/
	# "chunks()"
