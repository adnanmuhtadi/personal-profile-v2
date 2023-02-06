from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Views to pull all information from the database
# Projects are limited with only 9 items and ordered by date
def home(request):
    projects = Project.objects.all().order_by('-date_added')[:9]
    qualifications = Qualification.objects.all().order_by(
        '-completed_date')[:3]
    experiences = Experience.objects.all().order_by('-start_date')[:3]
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


###############################################################
# Views
# view to the admin side for the profile
# limited to only the superuser
def profileAdmin(request):
    return render(request, 'portfolio/profile_admin.html')


# view to the create options menu
def createEntry(request):
    return render(request, 'create/create_entry.html')


# view to the create options menu
def amendEntry(request):
    return render(request, 'amend/amend_entry.html')


###############################################################
# Experience
# view to create experience and adding it to the database
def createExperience(request):

    form = experienceForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = experienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create_entry/')

    context = {'form': form}
    return render(request, 'create/create_experience.html', context)


# view to the Amend Experiences
def amendExperience(request):
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences,
    }
    return render(request, 'amend/amend_experience.html', context)


# View to update the Experience
def updateExperience(request, pk):

    experience = Experience.objects.get(id=pk)
    form = experienceForm(instance=experience)

    if request.method == 'POST':
        print('Updating POST:', request.POST)
        form = experienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('/amend_experience/')

    context = {'form': form}
    return render(request, 'update/update_experience.html', context)


# Function to delete an experience
def deleteExperience(request, pk):
    experience = Experience.objects.get(id=pk)
    if request.method == "POST":
        experience.delete()
        return redirect('/amend_experience/')

    context = {'item': experience}
    return render(request, 'delete/delete_experience.html', context)


###############################################################
# Qualifications
# view to create qualification and adding it to the database
def createQualification(request):
    form = qualificationForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = qualificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create_entry/')

    context = {'form': form}
    return render(request, 'create/create_qualification.html', context)


# view to the Amend qualifications
def amendQualification(request):
    qualifications = Qualification.objects.all()
    context = {
        'qualifications': qualifications,
    }
    return render(request, 'amend/amend_qualification.html', context)


# update the qualifications
def updateQualification(request, pk):

    qualification = Qualification.objects.get(id=pk)
    form = qualificationForm(instance=qualification)

    if request.method == 'POST':
        print('Updating POST:', request.POST)
        form = qualificationForm(request.POST, instance=qualification)
        if form.is_valid():
            form.save()
            return redirect('/amend_qualification/')

    context = {'form': form}
    return render(request, 'update/update_qualification.html', context)


# Function to delete qualifications
def deleteQaulification(request, pk):
    qualification = Qualification.objects.get(id=pk)
    if request.method == "POST":
        qualification.delete()
        return redirect('/amend_qualification/')

    context = {'item': qualification}
    return render(request, 'delete/delete_qualification.html', context)


###############################################################
# Projects
# view to create project and adding it to the database
def createProject(request):
    form = projectForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/create_entry/')

    context = {'form': form}
    return render(request, 'create/create_project.html', context)


###############################################################
# Main Picture

# view to the Amend Main Picture
def amendMainPicture(request):
    mainpictures = MainPicture.objects.all()
    context = {
        'mainpictures': mainpictures,
    }
    return render(request, 'amend/amend_mainpicture.html', context)

# Update to main picture and adding it to the database
def updateMainPicture(request, pk):
    
    mainpicture = MainPicture.objects.get(id=pk)
    form = mainpictureForm(instance=mainpicture)
     
    if request.method == 'POST':
        print('Updating POST:', request.POST)
        form = mainpictureForm(request.POST, request.FILES, instance=mainpicture)
        if form.is_valid():
            form.save()
            return redirect('/amend_mainpicture/')

    context = {'form': form}
    return render(request, 'update/update_mainpicture.html', context)#


###############################################################
# About Picture

# view to the Amend About Picture
def amendAboutPicture(request):
    aboutpictures = AboutPicture.objects.all()
    context = {
        'aboutpictures': aboutpictures,
    }
    return render(request, 'amend/amend_aboutpicture.html', context)

# Update to about picture and adding it to the database
def updateAboutPicture(request, pk):
    
    aboutpicture = AboutPicture.objects.get(id=pk)
    form = aboutpictureForm(instance=aboutpicture)
     
    if request.method == 'POST':
        print('Updating POST:', request.POST)
        form = aboutpictureForm(request.POST, request.FILES, instance=aboutpicture)
        if form.is_valid():
            form.save()
            return redirect('/amend_aboutpicture/')

    context = {'form': form}
    return render(request, 'update/update_aboutpicture.html', context)