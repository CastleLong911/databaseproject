from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as lg, authenticate, logout
# Create your views here.

def login(request):
    return render(request, 'login.html', {})

def signout(request):
    logout(request)
    return redirect('index')

def signup_form(request):
    return render(request, 'signup.html', {})

def signup(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, '', password)
        user.save()
        user = authenticate(request, username=username, password=password)
        lg(request, user)
        return redirect('index')

def ajax_username_check(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
    else:
        username = request.POST['username']
        try:
            temp = User.objects.get(username=username)
            return JsonResponse({'result': 'disable'})
        except User.DoesNotExist:
            return JsonResponse({'result' : 'available'})
