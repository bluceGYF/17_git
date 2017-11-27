from django.shortcuts import render
from .models import *
from utils.wrappers import *
from .functions import *
from django.core.paginator import Paginator


def index(request):
    # 获取所有主分类
    cags = Goods_category.objects.all()
    # 最老商品（促销商品）
    old_goods = GoodsInfo.objects.all().order_by('-id')[:5]
    # 最热商品
    hot_goods = GoodsInfo.objects.all().order_by('-good_look')[:5]
    return render(request, 'goods/index.html', locals())


def product(request, a, cag_id, page_id):
    # 根据a的值来判断是按主分类取，还是子分类取,获得当前分类下面所有商品
    goods = get_goods_by_cag(a, cag_id)
    # 初始化分页器
    paginator = Paginator(goods, 10)
    current_page = paginator.page(page_id)
    page_id = int(page_id)
    return render(request, 'goods/product.html', locals())


def proinfo(request):
    # 获得商品
    goods = GoodsInfo.objects.get(pk=get(request, 'id'))
    goods_id = goods.id
    return render(request, 'goods/proinfo.html', locals())
