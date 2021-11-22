from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.forms.widgets import RadioSelect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from django.views import View
from django.shortcuts import render, redirect

from .forms.user_form import UserCreationForm
from .forms.loginform import LoginForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import User

class LoginView(View):
    def get(self, request):
        form=LoginForm()
        context={
            'form':form
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form=LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['password']
            user=authenticate(email=email, password=raw_password)
            if user is not None:
                if user.is_active and not user.is_superuser:
                    login(request,user)
                    request.session['user']=user.id
                    return redirect('index')
                else:
                    form.add_error('email','Invalid Email or password. Enter correct one')
            else:
                form.add_error('email','Invalid Email or password. Enter correct one')
            context={}
            context['form']=form
            return render(request,'login.html',context)
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
class RegisterView(View):
    def get(self, request):
        form=UserCreationForm()
        context={}
        context['form']=form
        return render(request, 'register.html', context)
    def post(self,request):
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            identifier=username+'eem'
            identifier=make_password(identifier)
            ident=identifier.split('/')
            id=''
            for i in ident:
                id=i+id
            user.identifier=id
            user.save()
            return redirect('login')
        return redirect('register')
class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')
    
    

