# from contextlib import redirect_stderr
from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Student_table
from .forms import Student_form
# Create your views here.
def index(request):
    return render(request, "student/index.html")

#   ----------------       CRUD  ----------------------

# get işlemi
def student_list(request):
    students=Student_table.objects.all()
    context={
        'students':students
    }
    return render(request, 'student/student_list.html',context)
    #   ----------------      create----------------------


def student_add(request):
    # form=Student_form()
    # if request.method=="POST":
    #     print(request.POST)

    form=Student_form(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect("list")
    
    context={
        'form':form
    }
    return render(request, 'student/student_add.html',context) 
     #   ----------------      update ----------------------


def student_update(request,id):
    
    student=Student_table.objects.get(id=id)

    form = Student_form(instance=student)

    if request.method=="POST":
        form=Student_form(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
    context={
        # 'student':student
        'form':form
    }
    return render(request,'student/student_update.html',context)

 #   ----------------      delete----------------------


def student_delete(request,id):
    student=Student_table.objects.get(id=id)
    if request.method=="POST":
        student.delete()
    context={
        'student':student
    }
    return render(request, 'student/student_delete.html',context) 