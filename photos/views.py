from django.http import HttpResponse
from django.shortcuts import render
from .models import Event

def index(request):
    all_events = Event.objects.all()
    context = {'all_events': all_events}
    return render(request, 'photos/index.html', context)

def detail(request, event_id):
    return HttpResponse("<h2>Details for event id: "+ str(event_id)+"</h2>")