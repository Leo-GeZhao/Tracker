from django.shortcuts import render, redirect
from .forms import PlanForm
from .models import Plan

# Create your views here.
def index(request):
    new_plan_form = PlanForm
    plans = Plan.objects.all()
    context = {
        'plans' : plans,
        "new_plan_form" : new_plan_form,
    }
    return render(request, 'index.html', context)

def add_plan(request):
    form = PlanForm(request.POST)
    if form.is_valid:
        new_form = form.save(commit=False)
        new_form.save()
    return redirect('index')

def plan_detail(request, plan_id):
    plan = Plan.objects.get(id = plan_id)
    context = {
        'plan' : plan,
    }
    return render(request,'plan_detail.html', context)

def delete_plan(request, plan_id):
    Plan.objects.get(id = plan_id).delete()
    return redirect('index')