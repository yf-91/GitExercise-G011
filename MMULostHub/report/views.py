from django.shortcuts import render

def feedback_view(request):
    return render(request, 'report/feedback.html')
