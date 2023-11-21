from django.shortcuts import render, redirect
from django.http import HttpResponse
from control.models import CAR, Student
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"control/index.html")
def about(request):
    return render(request,"control/about.html")
def contact(request):
    return render(request,"control/contact.html")

def car(request):
    car = CAR.objects.all()
    context = {
        'cars':car
    }
    return render(request,"control/car.html",context)
def add_car(request):
    if request.method == 'POST':
        carname = request.POST.get('car_name')
        carspeed = request.POST.get('car_speed')

        cars = CAR.objects.create(
            car_name = carname,
            speed = carspeed,
        )
        cars.save()
        messages.success(request,"Car successfully added")
        return redirect('/car')
    return render(request,"control/add_car.html")

def update_car(request,id):
    queryset = CAR.objects.get(id = id)
    if request.method == 'POST':
        carname = request.POST.get('car_name')
        carspeed = request.POST.get('car_speed')

        queryset.car_name = carname
        queryset.speed = carspeed
        queryset.save()
        messages.success(request,"Car updated successfully")
        return redirect('/car')
    context = {
        'cars':queryset
    }
    return render(request,"control/update_car.html",context)

def delete_car(request,id):
    queryset = CAR.objects.get(id = id)
    queryset.delete()
    messages.success(request,"Car successfully deleted")
    return redirect('/car')



def student(request):
    add = Student.objects.all()
    context = {
        'STUDENT':add
    }
    return render(request,"control/student.html",context)

def add_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        collages = request.POST.get('Collage')
        years = request.POST.get('year')
        streams = request.POST.get('stream')

        stu = Student.objects.create(
            name = student_name,
            collage = collages,
            year = years,
            stream = streams,
        )
        stu.save()
        print(student_name)
        print(collages)
        print(streams)
        print("hello world")
        messages.success(request,"Student Succussfully Added")
        return redirect('/add_student')
    
    return render(request,"control/add_student.html")

def delete_student(request,id):
    queryset = Student.objects.get(id = id)
    queryset.delete()
    messages.success(request,"Student delete successfully ")
    return redirect('/student')

def update_student(request,id):
    queryset = Student.objects.get(id = id)
    if request.method == "POST":
        student_name = request.POST.get('student_name')
        collages = request.POST.get('Collage')
        years = request.POST.get('year')
        streams = request.POST.get('stream')

        queryset.name = student_name
        queryset.collage = collages
        queryset.year = years
        queryset.stream = streams
        queryset.save()
        messages.success(request,"Student Updated Succussfully")
        return redirect('/student')
    context = {
        'student':queryset
    }
    return render(request,"control/update_student.html",context)