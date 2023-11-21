from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        passwd = request.POST.get('passwd')
        
    return render(request,"login.html")


def register(request):
    if request.method == "POST":
        first_names = request.POST.get('first_name')
        last_names = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        passwd = request.POST.get('passwd')

        #print(first_names)
        #print(request.POST)

        user = User.objects.filter(username = user_name)
        if user.exists():
            messages.info(request, 'username already taken')
            return redirect('/registers')

        user = User.objects.create(
            first_name = first_names,
            last_name = last_names,
            username = user_name,
            # password = passwd, # hum aisa kare hai too password encripte nahi hota hai
        )
        my_password = passwd
        User.set_password(my_password)
        user.save()
        messages.info(request, 'account created sucussfully')
        return redirect('/registers')
    return render(request,"register.html")