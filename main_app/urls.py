from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('add_plan/', views.add_plan, name='add_plan'),
    path('plan/<int:plan_id>/', views.plan_detail, name='plan_detail'),
    path('plan/<int:plan_id>/delete/', views.delete_plan, name='delete_plan'),
    path('plan/<int:pk>/update/', views.PlanUpdate.as_view(), name='update_plan'),
    path('plan/<int:plan_id>/add_priority', views.add_priority, name='add_priority'),

    path('plan/<int:plan_id>/add_progress', views.add_progress, name='add_progress'),
    path('plan/<int:plan_id>/delete_progress/<progress_id>', views.delete_progress, name='delete_progress'),
    path('plan/<int:plan_id>/update_is_complete/<progress_id>/', views.update_is_complete, name='update_is_complete'),
    
    
    
    
]