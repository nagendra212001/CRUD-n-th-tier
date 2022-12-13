from django.shortcuts import render

from django.db.models.functions import Length

# Create your views here.

from app.models import *

def topicdisplay(request):
    LTO=topic.objects.all()
    d={'LTO':LTO}
    return render(request,"topicdisplay.html",d)

def webpagedisplay(request):
    LWO=webpage.objects.all()
    
    LWO=webpage.objects.filter(topic_name='circket')
    LWO=webpage.objects.exclude(topic_name='football')
    LWO=webpage.objects.all()[1:4:]
    LWO=webpage.objects.all().order_by('topic_name')
    LWO=webpage.objects.all().order_by('-name')
    LWO=webpage.objects.all().order_by(Length('name'))
    LWO=webpage.objects.all().order_by(Length('name').desc())

    w={'LWO':LWO}
    return render(request,"webpagedisplay.html",w)

def accessdisplay(request):
    LAO=access_record.objects.all()
    a={'LAO':LAO}
    return render(request,"accessdisplay.html",a)