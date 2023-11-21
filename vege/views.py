from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def receipe(request):
    if request.POST:
        data = request.POST
        receipe_name = data.get('recipe_name')
        receipe_descriptions = data.get('recipe_description')
        receipe_images = request.FILES.get('recipe_image')

        receipe=RECEIPE.objects.create(
            receipe_name = receipe_name,
            receipe_descriptions = receipe_descriptions,
            receipe_iamge =  receipe_images,
        )
        receipe.save()
        print(receipe_name)
        print(receipe_descriptions)
        print(receipe_images)
        return redirect('/receipes')
    
    query = RECEIPE.objects.all()

    if request.GET.get('search'):
        #print(request.GET.get('search'))
        query = query.filter(receipe_name__icontains = request.GET.get('search'))

    context = {
        'receipes':query
    }
    return render(request,"receipe.html",context)
    
@login_required(login_url='/login')
def delete_receipe(request, id):
    #print(id)
    quesryset = RECEIPE.objects.get(id = id)
    quesryset.delete()
    return redirect('/receipes')


@login_required(login_url='/login')
def update_receipe(request, id):
    #print(id)
    queryset = RECEIPE.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        receipe_names = data.get('recipe_name')
        receipe_descriptionss = data.get('recipe_description')
        receipe_imagess = request.FILES.get('recipe_image')

        queryset.receipe_name = receipe_names
        queryset.receipe_descriptions = receipe_descriptionss

        if receipe_imagess:
            queryset.receipe_iamge = receipe_imagess

        queryset.save()
        return redirect('/receipes')
    
    context = {
        'receipe':queryset
    }

    return render(request,"update_receipe.html",context)


def login_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        if not User.objects.filter(username = user_name).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login')
        
        user = authenticate(username = user_name , password = password)

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/receipes')
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect('/login')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = User.objects.filter(username = user_name)
        
        if user.exists():
            messages.info(request,"username already taken")
            return redirect('/register')

        user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        username = user_name,
        )

        user.set_password(password)
        user.save()
        messages.success(request,"account created successfully")
        return redirect('/register')

    return render(request,"register.html")