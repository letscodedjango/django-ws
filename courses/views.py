from django.shortcuts import render, get_object_or_404
from .models import Courses

# Create your views here.

def home(request):
    courses = Courses.objects
    return render(request, 'courses/index.html', {'courses':courses})

def course_details(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    return render(request, 'courses/details.html', {'course': course})
