import csv






# The following example doesn't use chunks. We probably should.
# f is the file we got passed from the upload. It only exists in memory; we should NOT write it to disk.
def csv_import(f):
	dialect = csv.Sniffer().sniff(f.read(1024))
	f.seek(0)
	reader = csv.reader(f, dialect)
	for row in reader:
		
		pass

	# Parse the imported CSV file here
	# Reference: http://docs.djangoproject.com/en/1.2/topics/http/file-uploads/
	# "chunks()"

