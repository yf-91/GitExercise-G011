from django.shortcuts import render

def beginning(request):
    return render(request, 'user/beginning.html')

def user_login(request):
    return render(request, 'user/user-login.html')

def admin_login(request):
    return render(request, 'user/admin-login.html')

def register(request):
    return render(request, 'user/register.html')