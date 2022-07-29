from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
# Create your views here.


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        subject=request.POST['subject']
        message=request.POST['message']
        image=request.FILES['image']
        

        x=Customer(username=username,email=email,password=password,subject=subject,message=message,image=image)
        x.save()

    return render(request,'register/register.html',{})





