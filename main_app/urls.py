from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_plan/', views.add_plan, name='add_plan'),
    path('plan/<int:plan_id>/', views.plan_detail, name='plan_detail'),
    path('plan/<int:plan_id>/delete/', views.delete_plan, name='delete_plan')
]