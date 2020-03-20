from .models import Meeting, MeetingMinutes, Resource, Event
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def gettypes(request):
    type_list=Resource.objects.all()
    return render(request, 'club/resources.html' ,{'type_list' : type_list})
