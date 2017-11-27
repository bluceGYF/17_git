from django.db import models
from db.AbstractModel import *


# 购物车管理器类
class CartManager(models.Manager):
    pass


# 购物车模型类
class GoodsCart(AbstractModel):
    # 购物车商品
    cart_goods = models.ForeignKey('goods.GoodsInfo')
    # 购物车商品数量
    cart_amount = models.IntegerField()
    # 所属用户
    cart_user = models.ForeignKey('user.User')

    # 创建管理器
    objects = CartManager()


# 订单商品详情模型
class Order_GoodsDetails(AbstractModel):
    # 商品名字
    goods_name = models.CharField(max_length=50)
    # 商品价格
    goods_price = models.IntegerField()
    # 商品图片
    goods_image = models.ImageField()
    # 商品数量
    goods_num = models.IntegerField()
    # 商品单位
    goods_unit = models.CharField(max_length=10)
    # 商品所属订单
    goods_order = models.ForeignKey('Order')


# 订单基本信息模型
class Order(AbstractModel):
    status = (
        (1, '待付款'),
        (2, '代发货'),
        (3, '待收货'),
        (4, '已完成'),
    )
    pay = (
        (1, '网银支付'),
        (2, '信用卡支付'),
        (3, '财付通支付'),
        (4, '支付宝支付'),
    )
    # 订单编号
    order_number = models.CharField(max_length=50)
    # 订单状态
    order_status = models.SmallIntegerField(choices=status, default=1)
    # 订单收货人
    order_recv = models.CharField(max_length=20)
    # 订单收货地址
    order_addr = models.CharField(max_length=50)
    # 收货人电话
    order_tele = models.CharField(max_length=11)
    # 订单付款方式
    order_pay = models.SmallIntegerField(choices=pay, default=1)
    # 订单所属用户
    order_user = models.ForeignKey('user.User')
