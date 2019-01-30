from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('addorder/',views.add_order,name='add_order'),
    path('getorder/<int:order_id>',views.order,name='get_order'),
    path('deleteorder/',views.delete_order,name='delete_order'),
    path('changeorderstatus/',views.change_order_status,name='change_order_status'),
    path('multichangeorderstatus/',views.multi_change_order_status,name='multi_change_order_status'),
    path('export/',views.export_excel,name='export_excel')
]