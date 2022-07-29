
from django.urls import path 
from . import views

urlpatterns = [
path('registeration',views.signup,name='signup'),
]