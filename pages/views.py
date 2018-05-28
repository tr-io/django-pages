# imports
from django.shortcuts import render
# import templateview class
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html' # grab home.html template from templates directory

class AboutPageView(TemplateView):
    template_name = 'about.html'

