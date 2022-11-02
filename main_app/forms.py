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
            'description': forms.Textarea(attrs = {'style' : 'margin-top:10px;'}),
            "deadline": forms.DateInput(attrs = {'id' : 'id_deadline', 'type' : 'date'})
        }
class UpdatePlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['title','target','description', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs = {'readonly' : True, 'style' : 'border:none transparent; outline: none;'}),
            'target': forms.TextInput(attrs = {'readonly' : True, 'style' : 'border:none transparent; outline: none;', 'size' : 50}),
            'description': forms.Textarea(attrs = {'class' : 'form-control', 'style': 'width:400px; margin-top:10px;'}),
            "deadline": forms.DateInput(attrs = { 'type' : 'date', 'style' : 'margin-top:20px'})
        }
        

        