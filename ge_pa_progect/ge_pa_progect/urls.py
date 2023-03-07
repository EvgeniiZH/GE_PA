from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("password/", views.generate_password, name='generate-password'),
]
