from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from apps.home.models import *

def sort_all(request):
    type_list=SubClass.objects.all().values('name')
    locname_list=Loc.objects.all().values('name')
    year_list=Decade.objects.all().order_by('name').values('name')
    films=Film.objects.all()
    return render(request,'sort/sort_movies.html',locals())

def sort(request,type):
    type_list = SubClass.objects.all().values('name')
    locname_list = Loc.objects.all().values('name')
    year_list = Decade.objects.all().order_by('name').values('name')
    films=Film.objects.filter(Q(cata_log_name=type)|Q(sub_class_name=type)|Q(on_decade=type)|Q(loc_name=type))
    return render(request,'sort/sort_movies.html',locals())

