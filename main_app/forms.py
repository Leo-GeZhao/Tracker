from django import forms
from django.forms import ModelForm
from main_app.models import Plan, Progress

class DateInput(forms.DateInput):
    input_type = 'date'

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['category','title','target','description', 'deadline', 'is_priority']
        widgets = {
            'description': forms.Textarea(attrs = {'style' : 'margin-top:10px; border:1px solid black'}),
            "deadline": forms.DateInput(attrs = {'type' : 'date'}),
            'category': forms.Select(attrs = {'style': 'padding: 0 34px;'})
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

class ProgressForm(ModelForm):
    class Meta:
        model = Progress
        fields = ['progress', 'estimate_date']
        widgets = {
            "estimate_date": forms.DateInput(attrs = {'type' : 'date'})
        }

        