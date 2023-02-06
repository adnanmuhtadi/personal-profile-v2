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
    path('create_qualification/', views.createQualification,
         name="create_qualification"),
    path('create_project/', views.createProject, name="create_project"),

    # URLs to amend current information
    path('amend_entry/', views.amendEntry, name="amend_entry"),
    path('amend_experience/', views.amendExperience, name="amend_experience"),
    path('amend_qualification/', views.amendQualification,
         name="amend_qualification"),

    # URLs to Update current information
    path('update_experience/<str:pk>/',
         views.updateExperience, name="update_experience"),
    path('update_qualification/<str:pk>/',
         views.updateQualification, name="update_qualification"),

    # URLs to Delete current information
    path('delete_experience/<str:pk>/',
         views.deleteExperience, name="delete_experience"),
    path('delete_qualification/<str:pk>/',
         views.deleteQaulification, name="delete_qualification"),
]
