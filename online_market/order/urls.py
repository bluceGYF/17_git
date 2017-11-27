from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^order_details/$', views.order_details, name='order_details'),
]