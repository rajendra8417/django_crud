from django.shortcuts import render,redirect
from .models import*
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect




# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipes_images=request.FILES.get("reciepe_images")
        recepe_name=data.get("reciepe_name")
        desc=data.get("reciepe_description")
        print(recepe_name,desc,receipes_images)
        
        Reciepe.objects.create(
         reciepe_name=recepe_name,
         reciepe_description=desc,
         reciepe_image=receipes_images
         )
   
    
    queryset=Reciepe.objects.all()

    if request.GET.get('search'):
         queryset = queryset.filter(reciepe_name__icontains=request.GET.get('search'))
   


    return render(request,"receipes.html", context={"recipes":queryset})

def update_receipe(request, id):
    queryset = Reciepe.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST
        receipes_images = request.FILES.get("reciepe_images")
        recepe_name = data.get("reciepe_name")
        desc = data.get("reciepe_description")

        # Update the fields
        queryset.reciepe_name = recepe_name
        queryset.reciepe_description = desc
        if receipes_images:  # Only update the image if a new one is uploaded
            queryset.reciepe_image = receipes_images
        queryset.save()

        # Redirect after saving
        return redirect("/receipes/")

    # Render the update form with the existing recipe details
    return render(request, "update_receipe.html", {"recipe": queryset})



def delete_receipe(request,id):
    queryset=Reciepe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect(receipes)

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect ("/login/")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_page(request):
    if request.method == "POST":
        # Get data from POST request
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Create user
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"username already taken")
            return redirect("/register/") 

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        # Set user password and save the user
        user.set_password(password)
        user.save()
        messages.info(request,"username registerd")

        # Redirect to login page after successful registration
        return redirect("/login/")

    # Render the registration page
    return render(request, "register.html")


