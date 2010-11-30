# Create your views here.
from django.http import HttpResponse

def home(request):
    html = "<html><body>Test successful</body></html>"
    return HttpResponse(html)
