from django.urls import path
from . import views
from .views import admin_feedback_view

urlpatterns = [
    path('adminfeedback/', views.admin_feedback_view, name='admin_feedback'),
]