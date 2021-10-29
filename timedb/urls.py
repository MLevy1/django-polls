from django.urls import path

from . import views

app_name = 'timedb'

urlpatterns = [
    #main page
    path('', views.index, name='index'),

    #event list
    path('event_list/', views.event_list, name='event_list'),

    #activity list
    path('act_list/', views.act_list, name='act_list'),

    #activity detail
    path('act_detail/<int:act_id>/', views.act_detail, name='act_detail'),

    #sub project list
    path('subproj_list/', views.subproj_list, name='subproj_list'),

    #sub project detail
    path('subproj_detail/<int:subproj_id>/', views.subproj_detail, name='subproj_detail'),

    #event detail
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),

    #test
    path('tpage/', views.tpage, name='tpage'),
]