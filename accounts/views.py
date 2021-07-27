from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def SignInView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    account = authenticate(username=username, password=password)
    if account:
        login(request, account)
        if request.user.is_superuser:
            return redirect('/admin/')
        if request.user.is_staff and request.user.groups.filter(name='manager').exists():
            return render(request, 'registrations/manager.html')
        else:
            return redirect('/products')
    return render(request, 'registrations/login.html')