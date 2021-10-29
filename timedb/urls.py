from django.urls import path

from . import views

app_name = 'timedb'

urlpatterns = [
    #main page
    path('', views.index, name='index'),

    #LIST   

    #event list
    path('event_list/', views.event_list, name='event_list'),

    #activity list
    path('act_list/', views.act_list, name='act_list'),

    #sub project list
    path('subproj_list/', views.subproj_list, name='subproj_list'),

    #DETAIL

    #event detail
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),

    #activity detail
    path('act_detail/<int:act_id>/', views.act_detail, name='act_detail'),

    #sub project detail
    path('subproj_detail/<int:subproj_id>/', views.subproj_detail, name='subproj_detail'),

    #ADD

    #event add


    #activity add
    path('act_add/', views.act_add, name='act_add'),

    #sub project add


    #test
    path('tpage/', views.tpage, name='tpage'),

]