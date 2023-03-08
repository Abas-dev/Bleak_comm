from django.urls import path
from .views import HomePageView,AboutPageView,ProductDetailView,CartPageView

app_name = 'base'

urlpatterns = [
    path('',HomePageView.as_view(), name='homePage'),
    path('about/',AboutPageView.as_view(),name='aboutPage'),
    path('product/<int:pk>',ProductDetailView.as_view(),name='productDetail'),
    path('cart/',CartPageView.as_view(),name='cart'),
]