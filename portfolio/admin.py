from django.contrib import admin
from .models import Experience
from .models import Qualification
from .models import Project
from .models import MainPicture
from .models import AboutPicture


class ExperienceAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'title',
        'company',
        'location',
        'start_date',
        'finished_date',
    )


# Register your models here.
admin.site.register(Experience, ExperienceAdmin)


class QualificationAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'title',
        'from_where',
        'description',
        'completed_date',
    )


# Register your models here.
admin.site.register(Qualification, QualificationAdmin)


class ProjectAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'title',
        'meta_type',
        'image',
        'website_url',
        'github_url',
    )


# Register your models here.
admin.site.register(Project, ProjectAdmin)


class MainPictureAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'title',
        'image',
    )


# Register your models here.
admin.site.register(MainPicture, MainPictureAdmin)


class AboutPictureAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'title',
        'image',
    )


# Register your models here.
admin.site.register(AboutPicture, AboutPictureAdmin)
