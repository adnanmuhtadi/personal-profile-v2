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
    date_added = models.DateField()

    def __str__(self):
        return self.title


class Qualification(models.Model):
    title = models.CharField(max_length=100)
    from_where = models.CharField(max_length=200)
    description = models.TextField()
    completed_date = models.DateField()
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    present = models.BooleanField(default=False)
    finished_date = models.DateField(blank=True, null=True)
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class MainPicture(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/myself')

    def __str__(self):
        return self.title


class AboutPicture(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/myself')

    def __str__(self):
        return self.title
