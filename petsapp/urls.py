from django.urls import path

from petsapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin_index',views.admin_index, name='admin_index'),
    path('doctor_reg',views.doctor_reg, name='doctor_reg'),
    path('user_reg',views.user_reg, name='user_reg'),
]
