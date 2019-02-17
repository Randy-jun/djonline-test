from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('add_organization/',views.add_organization,name='add_organization'),
    path('get_organization/',views.get_organization,name='add_organization'),
    path('inactivate_org/',views.inactivate_organization,name='inactivate_org'),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('get_employee/',views.get_employee,name='add_employee'),
]