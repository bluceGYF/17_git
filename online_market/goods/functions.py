from .models import *


def get_goods_by_cag(a, cag_id):
    if a == '1':
        goods = GoodsInfo.objects.filter(good_cag_id=2)
        return goods
    if a == '2':
        goods = GoodsInfo.objects.filter(good_son_cag_id=cag_id)
        return goods
