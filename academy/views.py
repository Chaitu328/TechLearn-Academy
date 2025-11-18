from django.shortcuts import render

# Create your views here.
def course(request):
    return render(request, 'course.html')

def trainer(request):
    return render(request, 'trainer.html')

def student(request):
    return render(request, 'student.html')