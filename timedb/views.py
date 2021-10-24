from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>A New and Improved Time Database!</h1>")


def act_detail(request, act_id):
    return HttpResponse("You're looking at activity %s." %act_id)