from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from authApp.views import UserLoginView,UserLogoutView

from .models import Products,Catergory,Cart
from django.shortcuts import redirect,render

class HomePageView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Products
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['category'] = Catergory.objects.all()
        return context

class AboutPageView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'

class ProductDetailView(LoginRequiredMixin,DetailView):
    template_name = 'productDetail.html'
    model = Products
    context_object_name = 'productDes'

class CartPageView(LoginRequiredMixin,TemplateView):
    template_name = 'cart.html' 

# class AddCartView(LoginRequiredMixin,CreateView):
    

#     def post(self, request, *args, **kwargs):
#         user = request.user
#         product_id = request.GET.get('product_id')
#         product = Products.objects.get(id=product_id)
#         productQuantity = self.request.GET['quantity']
#         Cart(customer=user,product=product,quantity=productQuantity).save()
#         return redirect('base:homePage')

   
def add_cart(request):
    user = request.user 
    product_id = request.GET.get('product_id')
    product = Products.objects.get(id=product_id)
    # productQuantity = request.POST['quantity']
    Cart(customer=user,product=product).save()
    return redirect('base:homePage') 