from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', view.feedback_view, name='feedback'),
]