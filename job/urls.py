from django.urls import path
from . import views

app_name = 'job'
urlpatterns = [
    path('',views.job_list, name='job_list'),
    path('add/', views.add_job , name='add_job'),

    path('<str:slug>', views.job_details , name='job_details'),
    
    
    
]
