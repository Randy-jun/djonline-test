from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('request_form_list/', views.request_form_list,name='request_form_list'),
    path('request_form/<int:num>/',views.request_form,name='request_form'),
    path('new_request/add_new_request',views.add_new_request,name='add_new_request'),
    path('new_request/', views.new_request, name='new_request'),
    path('return_json/',views.return_json,name='return_json'),
    path('get_json/',views.get_json,name='get_json'),
    path('agencies/',views.orz_list,name='orz_list'),
    path('agency/<int:pk>/',views.orz_detail,name='orz_detail')
]
