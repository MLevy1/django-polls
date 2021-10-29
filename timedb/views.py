from django.shortcuts import render, get_object_or_404

from django.http import Http404

from django urs import reverse

from .models import Activity, SubProj, Event

from django.http import HttpResponse, HttpResponseRedirect

#main page
def index(request):
    return HttpResponse("<h1>A New and Improved Time Database!</h1>\
    <p>Comming Soon!</p>\
    <p><a href='./admin/'>Admin</a></p>\
    <p><a href='./event_list/'>Events</a></p>\
    <p><a href='./act_list'>Activities</a></p>\
    <p><a href='./subproj_list'>Sub Projects</a></p>")

#test page
def tpage(request):
    output = 'test'
    return HttpResponse(output)

#LISTS

#event list
def event_list(request):
    elist = Event.objects.order_by('-id')
    context = {'elist' : elist, }
    return render(request, 'timedb/event_list.html', context)

#activity list
def act_list(request):
    actlist = Activity.objects.order_by('-activity_name')
    context = {'actlist' : actlist, }
    return render(request, 'timedb/act_list.html', context)

#sub-project list
def subproj_list(request):
    splist = SubProj.objects.order_by('-subproj_name')
    context = {'splist' : splist,}
    return render(request, 'timedb/sp_list.html', context)

#DETAIL

#activity detail
def act_detail(request, act_id):
    activity = get_object_or_404(Activity, pk=act_id)
    return render(request, 'timedb/act_detail.html', { 'activity' : activity })

#sub-project detail
def subproj_detail(request, subproj_id):
    sp = get_object_or_404(SubProj, pk=subproj_id)
    return render(request, 'timedb/sp_detail.html', { 'subproj' : sp })

#event detail
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'timedb/event_detail.html', { 'event' : event })

#ADD

#add event


#add activity
def act_add(request):



#add sub-project


