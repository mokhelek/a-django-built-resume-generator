from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import logout, login, authenticate
from .models import Profile
from .forms import SignUpForm 

# Create your views here.
def register(request):
    if request.method != 'POST':
        form = SignUpForm ()
    else:
        form = SignUpForm (data=request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            login(request, new_user)
            return redirect('main_app:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

