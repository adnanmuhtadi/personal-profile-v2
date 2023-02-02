from django.urls import path
from . import views

urlpatterns = [
    # Set of empty path to indicate this is the route URL,
    # and its going to render views.index with the name Home.

    path('', views.home, name='home'),
    path('create_experience/', views.createExperience, name="create_experience"),
    path('create_project/', views.createProject, name="create_project"),
]
