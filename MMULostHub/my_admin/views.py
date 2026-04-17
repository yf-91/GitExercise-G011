from django.shortcuts import render

# Create your views here.
def admin_feedback_view(request):
    return render(request, 'my_admin/adminfeedback.html')
