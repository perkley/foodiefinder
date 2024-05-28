from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import login, logout
from django.contrib import messages
from django.conf import settings
from .forms import SignUpForm

# Create your views here.
def log_in_user(request):
    next = request.GET.get('next', '')
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'form':AuthenticationForm(), 'error':False})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password']) 
        if user is None:
            errorMsg = 'Email and/or password invalid.'
            form = AuthenticationForm(initial={'username': request.POST['username']})
            return render(request, 'registration/login.html', {'form':form, 'error':errorMsg})
        else:
            login(request, user)
         
            print('Permissions Listed')
            if user.is_superuser:
                print('All Permissions - Superuser')
            else:
                print(user.get_all_permissions())
            
            # if user.require_change_password:
            #     messages.add_message(request, messages.WARNING, 'You are required to change your password.')
            #     return redirect('password_change')

            if next == '':
                return redirect('home')
            else: return redirect(next) 

def log_out_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
