from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method== 'POST':
        username= request.POST['uname']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/home")
        else:
            messages.error(request,"Invalid Credentials")
            return render(request,"login.html")    
    else:
        return render(request, 'login.html')    



def register(request):
    if request.method== 'POST':
        ftname= request.POST['fname']
        ltname= request.POST['lname']
        urname= request.POST['uname']
        mailid= request.POST['mail']
        pass1= request.POST['ps1']
        pass2= request.POST['ps2']
        if pass1==pass2:
            if User.objects.filter(username=urname).exists():
                messages.info(request,'Username already taken.')
                return render(request,"register.html")
            elif User.objects.filter(email=mailid).exists():  
                messages.info(request,'E-mail already exists.')
                return render(request, "request.html")
            else:    
                user= User.objects.create_user(username=urname, password=pass1, email=mailid, first_name=ftname, last_name=ltname)
                user.save()
                print("user created")
                return redirect("/")

            
        else:
            messages.info(request,'Password not matching.')
            return render(request,"register.html")
            

    else:
        return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/home')