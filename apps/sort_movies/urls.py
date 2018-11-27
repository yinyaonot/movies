from django.conf.urls import url

from apps.sort_movies import views

urlpatterns = [
    url('sortall/', views.sort_all, name='sortall'),
    url('sort/(.*)', views.sort, name='sort')
]
