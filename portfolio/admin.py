from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'title',
        'meta_type',
        'image',
        'website_url',
        'gitpod_url',
    )


admin.site.register(Project, ProjectAdmin)
