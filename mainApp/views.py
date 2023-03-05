from django.views.generic.list import ListView
from django.views.generic import TemplateView 


class HomePageView(TemplateView):
    template_name = 'index.html'
