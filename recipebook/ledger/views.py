from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def recipe_list(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

# Create your views here.
