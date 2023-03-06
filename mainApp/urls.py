from django.urls import path
from .views import HomePageView,AboutPageView

app_name = 'base'

urlpatterns = [
    path('',HomePageView.as_view(), name='homePage'),
    path('about/',AboutPageView.as_view(),name='aboutPage'),
    
]