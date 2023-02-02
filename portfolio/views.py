from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-date_added')[:9]
    qualifications = Qualification.objects.all()
    experiences = Experience.objects.all()
    mainpictures = MainPicture.objects.all()
    aboutpictures = AboutPicture.objects.all()

    context = {
        'qualifications': qualifications,
        'projects': projects,
        'experiences': experiences,
        'mainpictures': mainpictures,
        'aboutpictures': aboutpictures,
    }

    return render(request, 'portfolio/home.html', context)


def createExperience(request):

    form = experienceForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = experienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'portfolio/create_experience.html', context)


def createProject(request):

    form = projectForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = projectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'portfolio/create_project.html', context)
