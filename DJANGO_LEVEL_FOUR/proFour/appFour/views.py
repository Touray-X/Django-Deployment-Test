from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'appFour/page1.html', {'text':'Im high now', 'number':123})

def page2(request):
    return render(request,'appFour/page2.html')

def relative_url(request):
    return render(request, 'appFour/relative_url_template.html')

def base(request):
    return render(request, 'appFour/base.html')
