from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^product/(\d+)/(\d+)/(\d+)/$', views.product, name='product'),
    url(r'^proinfo/$', views.proinfo, name='proinfo'),

]