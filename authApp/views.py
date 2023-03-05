from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import CreateView

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = ''

class UserRegistrationView(CreateView):
    template_name = 'register.html'
    model =  UserCreationForm
    
