from django.db import models
from django.urls import reverse

# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length = 50)
    target = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    deadline = models.DateField()
    create_date = models.DateField(auto_now_add = True)
    is_priority = models.BooleanField(default = False)
    
    def __str__(self):
        return f"{self.title} estimated to be complete at {self.deadline}, which is created on {self.create_date}"

    def get_absolute_url(self):
        return reverse('plan_detail', kwargs={'plan_id': self.id})
    
    class Meta:
        ordering = ['deadline']

class Progress(models.Model):
    progress = models.CharField(max_length = 100)
    estimate_date = models.DateField()
    create_deate = models.DateField(auto_now_add = True)
    plan = models.ForeignKey(Plan, on_delete = models.CASCADE)
    is_complete = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.progress} made on {self.create_deate} is estimated to be finished at {self.estimate_date}"
    
    class Meta:
        ordering = ['estimate_date']