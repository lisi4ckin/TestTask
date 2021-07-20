from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def SignInView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    account = authenticate(username=username, password=password)
    if account:
        login(request, account)
        return redirect('/')
    return render(request, 'registrations/login.html')