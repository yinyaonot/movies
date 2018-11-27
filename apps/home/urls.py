from django.conf.urls import url

from apps.home import views

urlpatterns = [
    url('movies/',views.movies,name='movies'),
    url(r'detail/(.*)',views.detail,name='detail'),
]