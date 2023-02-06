from django.forms import ModelForm
from .models import *


###############################################################
# form fields that are being called from the experience model
# called all fields
class experienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            'title',
            'company',
            'location',
            'start_date',
            'present',
            'finished_date',
        ]


###############################################################
# form fields that are being called from the qualification model
# called sum fields to add
class qualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = [
            'title',
            'from_where',
            'completed_date',
        ]


###############################################################
# form fields that are being called from the project model
# called all fields
class projectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'meta_type',
            'type',
            'image',
            'website_url',
            'github_url',
            'date_added',
        ]


###############################################################
# form fields that are being called from the Main Picture (Header image) model
# called all fields
class mainpictureForm(ModelForm):
    class Meta:
        model = MainPicture
        fields = [
            'title',
            'image',
        ]


###############################################################
# form fields that are being called from the About Picture (About image) model
# called all fields
class aboutpictureForm(ModelForm):
    class Meta:
        model = AboutPicture
        fields = [
            'title',
            'image',
        ]


###############################################################
# form fields that are being called from the CV side model
# called all fields
class MyCVForm(ModelForm):
    class Meta:
        model = MyCV
        fields = [
            'title',
            'myfile',
        ]
