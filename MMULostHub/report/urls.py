from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_form_view, name='feedback_form'),
]