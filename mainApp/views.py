from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from authApp.views import UserLoginView,UserLogoutView

from .models import Products,Catergory

class HomePageView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Products
    context_object_name = 'product'

class AboutPageView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'

class ProductDetailView(LoginRequiredMixin,DetailView):
    template_name = 'productDetail.html'

