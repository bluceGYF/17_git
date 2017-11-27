from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^order2/$', views.order2, name='order2'),
    url(r'^success/$', views.success, name='success'),
    url(r'^add_goods/$', views.add_goods, name='add_goods'),
    url(r'^edit_goods_num/$', views.edit_goods_num, name='edit_goods_num'),
    url(r'^delete_goods/$', views.delete_goods, name='delete_goods'),
    # 商品结算
    url(r'^cart_accounts/$', views.cart_accounts, name='cart_accounts'),
    url(r'^order_handle/$', views.order_handle, name='order_handle'),
]