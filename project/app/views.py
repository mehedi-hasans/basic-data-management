from django.shortcuts import redirect, render

from app.models import Student

# Create your views here.
def home(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')

        stu= Student(
            name = name,
            email = email,
            department = department,
        )
        print(stu)
        stu.save()
        return redirect('home')
    students = Student.objects.all()
    context = {
        'stu' : students
    }

    return render(request, 'index.html', context)


def detetePage(request, id):
    stu = Student.objects.filter(id=id)
    stu.delete()
    return redirect('home')

def editPage(request, id):
    stu = Student.objects.filter(id=id)
    context = {
        'ustu': stu
    }
    return render(request, 'editPage.html', context)

def updatePage(request, id):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        print(id)
        student= Student(
                id=id,
                name = name,
                email = email,
                department = department,
        )
        student.save()
        return redirect('home')


    # def deleteTeacher(request,id):
    # user=Teacher.objects.filter(id=id)
    # user.delete()
    # return redirect("teacherList")