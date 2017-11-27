from django.db import models
from db.AbstractModel import *
from tinymce.models import HTMLField


# 商品主分类
class Goods_category(AbstractModel):
    cag_name = models.CharField(max_length=30)


# 商品子分类
class Goods_son_category(AbstractModel):
    cag_name = models.CharField(max_length=30)
    cag_father = models.ForeignKey('Goods_category', default='')


# 商品管理器类
class GoodsInfoManager(models.Manager):
        pass


# 商品模型
class GoodsInfo(AbstractModel):
    # 商品名称
    good_name = models.CharField(max_length=50)
    # 商品单位
    good_unit = models.CharField(max_length=10)
    # 商品单价
    good_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 商品规格
    good_size = models.CharField(max_length=20)
    # 商品图片
    good_image = models.ImageField()
    # 商品描述
    good_desc = HTMLField()
    # 商品浏览数
    good_look = models.IntegerField(default=0)
    # 商品状态
    good_status = models.BooleanField(default=True)
    # 商品库存（是否有货）
    good_have = models.BooleanField(default=True)
    # 商品购买数
    good_sales = models.IntegerField(default=0)
    # 商品编号
    good_code = models.DecimalField(max_digits=10, decimal_places=0, default=999999)
    # 商品主分类
    good_cag = models.ForeignKey('Goods_category')
    # 商品子分类
    good_son_cag = models.ForeignKey('Goods_son_category')

    # 创建商品管理器对象
    objects = GoodsInfoManager()
