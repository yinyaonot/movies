from django.conf.urls import url

from apps.account import views

urlpatterns = [
    url('register/',views.register,name='register'),
    url('update/',views.update_view,name='update'),
    url('login/',views.login_view,name='login'),
    url('logout/',views.logout_view,name='logout'),
    url('mail/',views.hello_mail),
    url('active/',views.active_account),
    # url('capt/', views.code,name='capt'),
    url('ref/', views.refresh_code,name='ref'),
]