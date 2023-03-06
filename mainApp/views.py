from django.views.generic.list import ListView
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from authApp.views import UserLoginView,UserLogoutView

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

class AboutPageView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'

