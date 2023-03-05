from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.shortcuts import redirect


class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        username = self.request.POST['uName']
        email = self.request.POST['email']
        firstName = self.request.POST['fName']
        lastName = self.request.POST['lName']
        password = self.request.POST['password']
        passwordConf = self.request.POST['passwordConf']
        if password != passwordConf:
            messages.error(request, 'password do not match')
            return redirect('authApp:register')
        else:
            user = User.objects.create_user(username=username,email=email,first_name = firstName, last_name = lastName, password = password)
            user.save()
            messages.success(request, 'your account has been created successfully')
            return redirect('authApp:login')
        

class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you have logged into your account')
            return redirect('base:homePage')
        else:
            messages.error(request,'cant login, try again.')
            return redirect('authApp:login')
class UserLogoutView(LogoutView):
    next_page = 'authApp:login'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)
    
        