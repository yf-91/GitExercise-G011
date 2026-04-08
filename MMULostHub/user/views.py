from django.shortcuts import render

def beginning(request):
    return render(request, 'beginning.html')