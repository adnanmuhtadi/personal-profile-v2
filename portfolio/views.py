from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request):
    projects = Project.objects.all()[:9]
    return render(request, 'portfolio/home.html', {'projects': projects})
