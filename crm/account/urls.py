from django.urls import path
from . import views

urlpatterns = [
    path('', views.signUp, name= 'SignUp')
]