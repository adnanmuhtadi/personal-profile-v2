from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Views to pull all information from the database
# Projects are limited with only 9 items and ordered by date
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


# view to the admin side for the profile
# limited to only the superuser
def profileAdmin(request):
    return render(request, 'portfolio/profile_admin.html')


# view to the create options menu
def createEntry(request):
    return render(request, 'create/create_entry.html')


# view to create experience and adding it to the database 
def createExperience(request):

    form = experienceForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = experienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'create/create_experience.html', context)


# view to create project and adding it to the database
def createProject(request):

    form = projectForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = projectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'create/create_project.html', context)


# view to create qualification and adding it to the database
def createQualification(request):

    form = qualificationForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = projectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'create/create_qualification.html', context)
