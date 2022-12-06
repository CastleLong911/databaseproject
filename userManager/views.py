from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def ajax_username_check(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
    else:
        print('username check!')
        username = request.POST['username']
        try:
            temp = User.objects.get(username=username)
            return JsonResponse({'result': 'disable'})
        except User.DoesNotExist:
            return JsonResponse({'result' : 'available'})
