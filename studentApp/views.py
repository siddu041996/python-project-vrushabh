from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Student

# Create your views here.

class StudentListView(ListView):
    template_name = 'studentApp/student_list.html'
    model = Student


def StudentData(request):
    if request.method == "POST":
        StudentData = Student()
        StudentData.first_name  = request.POST['first_name']
        StudentData.last_name   = request.POST['last_name']
        StudentData.test_score  = request.POST['test_score']
        StudentData.save()

        return redirect('../')
    else:
        # return render(request, 'genres_add.html',{'is_admin':is_admin})
        return render(request, 'studentApp/add_data.html')
