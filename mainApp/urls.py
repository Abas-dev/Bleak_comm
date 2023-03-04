from django.urls import path
from .views import homeTest

app_name = 'base'

urlpatterns = [
    path('',homeTest, name='test')
]