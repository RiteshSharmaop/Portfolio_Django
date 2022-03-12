from django.shortcuts import render , redirect
from .models import Contact
# Create your views here.
def home(request):
    if request.method == "POST":
        # print("ok")
        # print("This is post")
        name= request.POST["name"]
        email= request.POST["email"]
        phone= request.POST["phone"]
        desc= request.POST["desc"]
        # print(name,email,phone,desc)

        contact= Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request,'index.html')

    
