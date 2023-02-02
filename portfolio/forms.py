from django.forms import ModelForm
from .models import *


class experienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'


class projectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class qualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = ['title', 'from_where', 'completed_date']
