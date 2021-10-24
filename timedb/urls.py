from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:act_id>/', views.act_detail, name='detail'),
]