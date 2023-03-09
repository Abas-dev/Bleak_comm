from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Products,Cart
from django.shortcuts import redirect
from django.urls import reverse_lazy

    
class HomePageView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Products
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['cartNum'] = len(Cart.objects.filter(customer= self.request.user))
        return context

class AboutPageView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['cartNum'] = len(Cart.objects.filter(customer= self.request.user))
        return context

class ProductDetailView(LoginRequiredMixin,DetailView):
    template_name = 'productDetail.html'
    model = Products
    context_object_name = 'productDes'

    def post(self, request, *args, **kwargs):
        user = request.user 
        product_id = self.request.GET.get('product_id')
        product = Products.objects.get(id=product_id)
        Cart(customer=user,product=product).save()
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['cartNum'] = len(Cart.objects.filter(customer= self.request.user))
        return context
    
def add_cart(request):
    user = request.user 
    product_id = request.GET.get('product_id')
    product = Products.objects.get(id=product_id)
    Cart(customer=user,product=product).save()
    return redirect('base:homePage')     

class CartPageView(LoginRequiredMixin,TemplateView):
    template_name = 'cart.html' 
    model = Cart
    
    def get_context_data(self, **kwargs):
        context = super(CartPageView, self).get_context_data(**kwargs)
        context['cartItem'] = Cart.objects.filter(customer= self.request.user)
        context['cartNum'] = len(Cart.objects.filter(customer= self.request.user))
        return context
    
class CartDeleteView(LoginRequiredMixin,DeleteView):
    model = Cart
    context_object_name ='deleteCart'
    template_name = 'confirmDelete.html'
    success_url = reverse_lazy('base:cart')

    