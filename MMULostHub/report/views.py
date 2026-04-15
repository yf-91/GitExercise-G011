from django.shortcuts import render, redirect
from  .services import create_feedback

def feedback_view(request):
    if request.method == "POST":
        comments = request.POST.get('comments')
        image = request.FILES.get('image-upload') 

        #call service function
        create_feedback(comments=comments, image=image)

        return render(request, 'report/feedback.html', {'success': True})
    
    return render(request, 'report/feedback.html')
