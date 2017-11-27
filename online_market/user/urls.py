from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vip/$', views.vip, name='vip'),
    url(r'^city_change/$', views.city_change, name='city_change'),
    url(r'^vip_adress/$', views.vip_adress, name='vip_adress'),
    url(r'^use_detail/$', views.use_detail, name='use_detail'),
    url(r'^info/$', views.info, name='info'),
    url(r'^uorder/$', views.uorder, name='uorder'),
    url(r'^repwd/$', views.repwd, name='repwd'),
    url(r'^state/$', views.state, name='state'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout_handle/$', views.logout_handle, name='logout_handle'),
    url(r'^reg/$', views.reg, name='reg'),
    url(r'^message/$', views.message, name='message'),
    url(r'^check_username/$', views.check_username, name='check_username'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^check_yanzheng/$', views.check_yanzheng, name='check_yanzheng'),
    url(r'^user_edit_addr/$', views.user_edit_addr, name='user_edit_addr'),
    url(r'^verification_code/\d+/$', views.verification_code, name='verification_code'),
]