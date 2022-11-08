from django.shortcuts import render, redirect

from .forms import PlanForm, UpdatePlanForm, ProgressForm
from .models import Plan, Progress
from django.views.generic import UpdateView


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
    new_progress_form = ProgressForm
    complete_progress_count = Plan.objects.get(id = plan_id).progress_set.filter(is_complete = True).count()
    progress_count = Plan.objects.get(id= plan_id).progress_set.all().count()
    if progress_count:
        complete_percentage = round((complete_progress_count/progress_count) * 100,2)
    else:
        complete_percentage = 0
    context = {
        'plan' : plan,
        'new_progress_form' : new_progress_form,
        'progress_count' : progress_count,
        'complete_progress_count' : complete_progress_count,
        'complete_percentage' : complete_percentage,
    }
    return render(request,'plan_detail.html', context)

def delete_plan(request, plan_id):
    Plan.objects.get(id = plan_id).delete()
    return redirect('index')

def add_priority(request, plan_id):
    plan = Plan.objects.filter(id = plan_id)
    plan_is_priority = Plan.objects.values_list('is_priority',flat = True).get(id = plan_id)
    if plan_is_priority:
        plan.update(is_priority = False)
    else:
        plan.update(is_priority = True)
    return redirect('index')

class PlanUpdate(UpdateView):
    model = Plan
    form_class = UpdatePlanForm
    template_name = 'update_plan.html'

def add_progress(request, plan_id):
    form = ProgressForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.plan_id = plan_id
        new_form.save()
    return redirect('plan_detail', plan_id = plan_id)

def delete_progress(request, plan_id, progress_id,):
    progress = Progress.objects.filter(id = progress_id).delete()
    return redirect('plan_detail', plan_id = plan_id)

def update_is_complete(request,plan_id,progress_id):
    progress = Progress.objects.filter(id = progress_id)
    # progress_is_complete = Progress.objects.filter(id = progress_id).values('is_complete')
    progress_is_complete = Progress.objects.values_list('is_complete',flat = True).get(id = progress_id)
    if progress_is_complete:
        progress.update(is_complete = False)
    else:
        progress.update(is_complete = True)
    return redirect('plan_detail', plan_id = plan_id,)
    