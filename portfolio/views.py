from django.shortcuts import render
from .models import Project, Qualification, Experience, MainPicture, AboutPicture


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
