from django.urls import path
from . import views


urlpatterns = [
    path('adminfeedback', views.admin_feedback_view, name='admin_feedback'),
]