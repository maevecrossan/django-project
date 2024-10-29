from django.shortcuts import render
from django.http import HttpResponse
from hello_world import views as index_views

# Create your views here.
def index(request):
    if request.method == POST:
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)