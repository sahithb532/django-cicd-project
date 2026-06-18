from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request,'students/home.html',{
        'students':students
    })

def add_student(request):

    if request.method == 'POST':

        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course']
        )

        return redirect('/')

    return render(request,'students/add_student.html')
