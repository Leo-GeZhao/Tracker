from django import forms
from django.forms import ModelForm
from main_app.models import Plan

class DateInput(forms.DateInput):
    input_type = 'date'

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs = {}),
            "deadline": forms.DateInput(attrs = {'id' : 'id_deadline', 'type' : 'date'})
        }
        

        