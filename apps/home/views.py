from django.shortcuts import render

# Create your views here.
from apps.home.models import Film, Res


def home_page(request):
    return render(request,'home_page.html')
def movies(request):

    tvs = Film.objects.filter(cata_log_name='电视剧')[0:12]
    movies = Film.objects.filter(cata_log_name='电影')[0:12]
    cartoons = Film.objects.filter(cata_log_name='动漫')[0:12]
    tvs_list = Film.objects.filter(cata_log_name='电视剧').order_by('raty__score')[0:12]
    movies_list = Film.objects.filter(cata_log_name='电影').order_by('raty__score')[0:12]
    cartoons_list = Film.objects.filter(cata_log_name='动漫').order_by('raty__score')[0:12]
    return render(request, 'home/movie.html', locals())
def detail(request,id):
    film=Film.objects.get(id=id)
    res=Res.objects.filter(film_id=id).first()
    return render(request,'home/detail.html',context={'film':film,'res':res})


