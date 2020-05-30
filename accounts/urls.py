from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    
    path("register", v.register),
    path("login", v.login),
    path("logout", v.logout),
    
]
