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
    mycvs = MyCV.objects.all()

    context = {
        'experiences': experiences,
        'qualifications': qualifications,
        'projects': projects,
        'mainpictures': mainpictures,
        'aboutpictures': aboutpictures,
        'mycvs': mycvs,
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

    # Checking if the form is POST
    if request.method == 'POST':
        form = experienceForm(request.POST)
        print('Printing POST:', request.POST)

        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.company = request.POST["company"].title()
            data.location = request.POST["location"].title()
            data.save()
            return redirect('/create_entry/')
    else:
        form = experienceForm()

    context = {'form': form}
    return render(request, 'create/create_experience.html', context)


# view to the Amend Experiences
def amendExperience(request):
    # Displaying all the option in the list
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences,
    }
    return render(request, 'amend/amend_experience.html', context)


# View to update the Experience
def updateExperience(request, pk):

    # setting an id for each object pk
    experience = Experience.objects.get(id=pk)
    form = experienceForm(instance=experience)

    # checking if the form is POST
    if request.method == 'POST':
        form = experienceForm(request.POST, instance=experience)
        print('Updating POST:', request.POST)
        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.company = request.POST["company"].title()
            data.location = request.POST["location"].title()
            data.save()
            return redirect('/amend_experience/')
    else:
        data = experienceForm()

    context = {'form': form}
    return render(request, 'update/update_experience.html', context)


# Function to delete an experience
def deleteExperience(request, pk):

    # Setting the id for each object pk
    experience = Experience.objects.get(id=pk)
    # Checking if the form is POST
    if request.method == "POST":
        experience.delete()
        return redirect('/amend_experience/')

    context = {'item': experience}
    return render(request, 'delete/delete_experience.html', context)


###############################################################
# Qualifications
# view to create qualification and adding it to the database
def createQualification(request):

    # Checking if the form is POST
    if request.method == 'POST':
        form = qualificationForm(request.POST)
        print('Printing POST:', request.POST)

        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.from_where = request.POST["from_where"].title()
            data.save()
            return redirect('/create_entry/')
    else:
        form = qualificationForm()

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

    # Setting the Id for each object pk
    qualification = Qualification.objects.get(id=pk)
    form = qualificationForm(instance=qualification)

    # Checking if the form is POST
    if request.method == 'POST':
        form = qualificationForm(request.POST, instance=qualification)
        print('Updating POST:', request.POST)
        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.from_where = request.POST["from_where"].title()
            data.save()
            return redirect('/amend_qualification/')
    else:
        data = qualificationForm()

    context = {'form': form}
    return render(request, 'update/update_qualification.html', context)


# Function to delete qualifications
def deleteQaulification(request, pk):

    # Setting the ID for each object pk
    qualification = Qualification.objects.get(id=pk)
    # Checking if the form is POST
    if request.method == "POST":
        qualification.delete()
        return redirect('/amend_qualification/')

    context = {'item': qualification}
    return render(request, 'delete/delete_qualification.html', context)


###############################################################
# Projects
# view to create project and adding it to the database
def createProject(request):

    # Checking if the form method is POST
    if request.method == 'POST':
        # request.files is take the URL of the file and post it in Django
        form = projectForm(request.POST, request.FILES)
        print('Printing POST:', request.POST)

        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.description = request.POST["title"].capitalize()
            data.save()
            return redirect('/create_entry/')
    else:
        form = projectForm()

    context = {'form': form}
    return render(request, 'create/create_project.html', context)


# view to the Amend Experiences
def amendProject(request):
    # Displaying all the option in the list
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'amend/amend_project.html', context)


# update the qualifications
def updateProject(request, pk):

    # Setting the Id for each object pk
    project = Project.objects.get(id=pk)
    form = projectForm(instance=project)

    # Checking if the form is POST
    if request.method == 'POST':
        form = projectForm(request.POST, instance=project)
        print('Updating POST:', request.POST)
        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.save()
            return redirect('/amend_project/')
    else:
        data = projectForm()

    context = {'form': form}
    return render(request, 'update/update_project.html', context)


# Function to delete qualifications
def deleteProject(request, pk):

    # Setting the ID for each object pk
    project = Project.objects.get(id=pk)
    # Checking if the form is POST
    if request.method == "POST":
        project.delete()
        return redirect('/amend_project/')

    context = {'item': project}
    return render(request, 'delete/delete_project.html', context)


###############################################################
# Main Picture
# view to the Amend Main Picture
def amendMainPicture(request):
    # getting all the items from the database and putting in the method
    mainpictures = MainPicture.objects.all()
    context = {
        'mainpictures': mainpictures,
    }
    return render(request, 'amend/amend_mainpicture.html', context)


# Update to main picture and adding it to the database
def updateMainPicture(request, pk):

    # Setting an ID for each object pk
    mainpicture = MainPicture.objects.get(id=pk)
    form = mainpictureForm(instance=mainpicture)
    # Checking if the form method is POST
    if request.method == 'POST':
        print('Updating POST:', request.POST)
        # request.files is take the URL of the file and post it in Django
        form = mainpictureForm(
            request.POST, request.FILES, instance=mainpicture)
        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.save()
            return redirect('/amend_mainpicture/')
    else:
        data = mainpictureForm()

    context = {'form': form}
    return render(request, 'update/update_mainpicture.html', context)


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

    # Setting and ID for each object pk
    aboutpicture = AboutPicture.objects.get(id=pk)
    form = aboutpictureForm(instance=aboutpicture)
    # Checking if the form method is POST
    if request.method == 'POST':
        print('Updating POST:', request.POST)
        # request.files is take the URL of the file and post it in Django
        form = aboutpictureForm(
            request.POST, request.FILES, instance=aboutpicture)
        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.save()
            return redirect('/amend_aboutpicture/')
    else:
        data = aboutpictureForm()

    context = {'form': form}
    return render(request, 'update/update_aboutpicture.html', context)


###############################################################
# My CV

# view to the Amend About Picture
def amendMyCV(request):
    mycvs = MyCV.objects.all()
    context = {
        'mycvs': mycvs,
    }
    return render(request, 'amend/amend_cv.html', context)


# Update to about picture and adding it to the database
def updateMyCV(request, pk):

    # Setting and ID for each object pk
    mycv = MyCV.objects.get(id=pk)
    form = MyCVForm(instance=mycv)

    # checking the form method is POST
    if request.method == 'POST':
        print('Updating POST:', request.POST)
        # request.files is take the URL of the file and post it in Django
        form = MyCVForm(request.POST, request.FILES, instance=mycv)
        # Checking if the form is valid before saving it and posting to the django
        if form.is_valid():
            data = form.save(commit=False)
            # adding .title() at the end of each data field to define how it will be posted.
            data.title = request.POST["title"].title()
            data.save()
            return redirect('/amend_cv/')
    else:
        data = MyCVForm()

    context = {'form': form}
    return render(request, 'update/update_cv.html', context)
