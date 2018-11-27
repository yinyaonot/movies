from django.conf.urls import url,include
from django.contrib import admin

from apps.home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('home/',include('home.urls') ),
    url('account/',include('account.urls') ),
    url(r'^captcha/',include('captcha.urls') ),
    url(r'sort_movies/',include('sort_movies.urls') ),
    url('^$',views.home_page)
]
