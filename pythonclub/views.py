from .models import Meeting, MeetingMinutes, Resource, Event
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def getresources(request):
    type_list=Resource.objects.all()
    return render(request, 'club/resources.html' ,{'type_list' : type_list})

def getmeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meeting.html' ,{'meeting_list' : meeting_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meet
    }
    return render(request, 'club/meetdetails.html', context=context)