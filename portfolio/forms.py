from django.forms import ModelForm
from .models import *


# form fields that are being called from the experience model
# called all fields
class experienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'


# form fields that are being called from the qualification model
# called sum fields to add
class qualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = ['title', 'from_where', 'completed_date']


# form fields that are being called from the project model
# called all fields
class projectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
