from django.shortcuts import render
from django.http import HttpResponse
from about import views as about_views

# Create your views here.
def about_me(request):
    return HttpResponse("This would be the about page")