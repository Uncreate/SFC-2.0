from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .models import ToolOrder

def tool_builder(request):
    all_items = ToolOrder.objects.all
    return render(request, 'tooling/tool_builder.html', {'all_items' : all_items})

def home(request):
    return render(request, 'authenticate/home.html', {})
