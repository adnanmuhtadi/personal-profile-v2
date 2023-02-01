from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    meta_type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/work')
    website_url = models.URLField(blank=True)
    gitpod_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
