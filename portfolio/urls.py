from django.urls import path
from . import views

urlpatterns = [
    # Set of empty path to indicate this is the route URL,
    # and its going to render views.index with the name Home.

    path('', views.home, name='home'),
    path('profile_admin/', views.profileAdmin, name="profile_admin"),

    # URLs to Create new information to the profile
    path('create_entry/', views.createEntry, name="create_entry"),
    path('create_experience/', views.createExperience, name="create_experience"),
    path('create_project/', views.createProject, name="create_project"),
    path('create_qualification/', views.createQualification,
         name="create_qualification"),
]
