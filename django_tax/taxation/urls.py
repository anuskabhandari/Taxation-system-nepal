from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
 path('add/', views.add_employee, name='add_employee'),
    path('update/', views.update_employee, name='update_employee'),
    path('report/', views.view_report, name='view_report'),
]