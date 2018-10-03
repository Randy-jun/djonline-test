from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
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
    path('agency/<int:pk>/',views.orz_detail,name='orz_detail'),
    path('lineprices/',views.line_list,name='line_list'),
    path('lineprice/<int:pk>/',views.line_detail,name='line_detail'),
    path('refprices/',views.Ref_PriceList.as_view(),name='PriceList'),
    path('refdetail/<int:pk>/',views.Ref_PriceDetail.as_view(),name='PriceDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)