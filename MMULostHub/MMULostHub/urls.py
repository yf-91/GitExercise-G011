"""
URL configuration for MMULostHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from my_admin import views
from django.conf import settings
from django.conf.urls.static import static
=======
from django.urls import path
from django.urls import include
from user import views
>>>>>>> f1711a46efc951dfd0d5fd4cce6cd18bcf158e4c

urlpatterns = [
    path('', views.beginning, name='beginning'),
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('report/',include('report.urls')),
<<<<<<< HEAD
    path('adminfeedback/', views.admin_feedback_view, name='admin_feedback'),
=======
    path("user/", include("user.urls")),
>>>>>>> f1711a46efc951dfd0d5fd4cce6cd18bcf158e4c
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
