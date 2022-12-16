from django.shortcuts import render

from django.db.models.functions import Length

# Create your views here.
from django.db.models import Q
from app.models import *

def topicdisplay(request):
    LTO=topic.objects.all()
    LTO=topic.objects.filter(topic_name__contains="f")
    
    
    
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
    LWO=webpage.objects.all()

    LWO=webpage.objects.filter(name__startswith="r")
    LWO=webpage.objects.filter(url__endswith="com")
    LWO=webpage.objects.filter(name__contains="h")
    LWO=webpage.objects.filter(name__regex="r\w{6}")
    LWO=webpage.objects.filter(Q(name__startswith='r') & Q(url__endswith="com"))
    LWO=webpage.objects.all()

    w={'LWO':LWO}
    return render(request,"webpagedisplay.html",w)

def accessdisplay(request):
    LAO=access_record.objects.all()

    LAO=access_record.objects.filter(date__month='02')
    LAO=access_record.objects.filter(date__year='1991')
    LAO=access_record.objects.filter(date__day='05')
    LAO=access_record.objects.all()
    LAO=access_record.objects.filter(date__gt='1990-01-21')
    LAO=access_record.objects.filter(date__lt='1990-01-21')
    LAO=access_record.objects.filter(date__gte='1990-01-21')
    LAO=access_record.objects.filter(date__lte='1990-01-21')


    a={'LAO':LAO}
    return render(request,"accessdisplay.html",a)


def update_webpage(request):
    LWO=webpage.objects.all()
    webpage.objects.filter(name="rahul").update(url="http://kabaddi.in")
    t=topic.objects.get_or_create(topic_name="circket")[0]
    t.save()
    webpage.objects.update_or_create(name="SKY",defaults={'topic_name':t,'url':"http://skycricket.in"})
    webpage.objects.update_or_create(name="king kohli",defaults={'topic_name':t,'url':"http://cricket.in"})
    k=topic.objects.get_or_create(topic_name="boxing")[0]
    webpage.objects.update_or_create(topic_name=k,defaults={'name':"rahul",'url':'http://rahulboxing.in'})
    LWO=webpage.objects.all()
    w={'LWO':LWO}
    return render(request,"webpagedisplay.html",w)


def delete_webpage(request):
    LWO=webpage.objects.all()
   
    #webpage.objects.all().delete()
    
    webpage.objects.filter(name='praveen').delete()
    LWO=webpage.objects.all()
    
    d={'LWO':LWO}
    return render(request,"webpagedisplay.html",d)





