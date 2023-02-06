from django.db import models


# model for Experience
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    present = models.BooleanField(default=False)
    finished_date = models.DateField(blank=True, null=True)
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


# model for Qualifications
class Qualification(models.Model):
    title = models.CharField(max_length=100)
    from_where = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed_date = models.DateField()
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


# model for Projects
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=200)
    meta_type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/work', null=True, blank=True)
    website_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    date_added = models.DateField()

    def __str__(self):
        return self.title


# model for the Main picture
class MainPicture(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/myself')

    def __str__(self):
        return self.title


# model for the Picture in the about section
class AboutPicture(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/myself')

    def __str__(self):
        return self.title
