from django.shortcuts import render
from django.http import JsonResponse
from utils.wrappers import *
from .models import *
from user.functions import *
import time
import random
from django.db import transaction


@check_permission
def cart(request):
    user_id = get_session(request, 'uid')
    carts = GoodsCart.objects.filter(cart_user_id=user_id)
    carts.money = 0
    for cart in carts:
        # 单品总价
        cart.signal_money = cart.cart_goods.good_price*cart.cart_amount
        carts.money += cart.signal_money
    return render(request, 'cart/cart.html', locals())


@check_permission
def order2(request):
    return render(request, 'cart/order2.html', locals())


@check_permission
def success(request):
    return render(request, 'cart/success.html', locals())


# 添加商品视图
def add_goods(request):
    # 获得用户id
    user_id = get_session(request, 'uid')
    if user_id:
        # 获得商品id
        good_id = get(request, 'goods_id')
        # 获得商品数量
        good_amount = get(request, 'amount')
        # print(user_id)

        # 判断该商品是否已经在购物车中
        try:
            cart = GoodsCart.objects.get(cart_goods_id=good_id, cart_user_id=user_id)
            cart.cart_amount = cart.cart_amount + int(good_amount)
            cart.save()
        except GoodsCart.DoesNotExist:
            cart = GoodsCart()
            cart.cart_goods_id = good_id
            cart.cart_user_id = user_id
            cart.cart_amount = good_amount
            cart.save()

        # 返回给商品页面购物车商品的总数
        # total = GoodsCart.objects.filter(cart_user_id=user_id).aggregate(models.Sum('cart_amount'))
        carts = GoodsCart.objects.filter(cart_user_id=user_id)
        total = 0
        money = 0
        for cart in carts:
            signal = cart.cart_goods.good_price*cart.cart_amount
            money += signal
            total += cart.cart_amount
        return JsonResponse({'total': total, 'money': money, 'status': 1})
    else:
        return JsonResponse({'total': 0, 'money': 0, 'status': 0})


# 更新后台商品数量
def edit_goods_num(request):
    goods_id = get(request, 'goods_id')
    goods_num = get(request, 'goods_num')
    print(goods_id)
    print(goods_num)
    try:
        cart = GoodsCart.objects.get(cart_user_id=get_session(request, 'uid'), cart_goods_id=goods_id)
        cart.cart_amount = goods_num
        cart.save()
        return JsonResponse({'ret': 1})
    except GoodsCart.DoesNotExist:
        pass


# 删除删除商品
def delete_goods(request):
    goods_id = get(request, 'goods_id')
    user_id = get_session(request, 'uid')
    try:
        cart = GoodsCart.objects.get(cart_user_id=user_id, cart_goods_id=goods_id)
        cart.delete()
        # # 返回当下用户购物车商品的总数和总价
        # carts = GoodsCart.objects.filter(cart_user_id=user_id)
        # total = 0
        # money = 0
        # for cart in carts:
        #     signal = cart.cart_goods.good_price * cart.cart_amount
        #     money += signal
        #     total += cart.cart_amount
        return JsonResponse({'ret': 1})
    except GoodsCart.DoesNotExist:
        pass


# 商品结算
def cart_accounts(request):
    goods_ids = post_list(request, 'goods_id')
    goods_id_list = ','.join(goods_ids)
    # print(goods_ids)
    carts = GoodsCart.objects.filter(cart_user_id=get_session(request, 'uid'), cart_goods_id__in=goods_ids)
    carts.total_num = 0
    carts.total_money = 0
    for cart in carts:
        carts.total_num += cart.cart_amount
        cart.signal_money = cart.cart_goods.good_price*cart.cart_amount
        carts.total_money += cart.signal_money
    return render(request, 'cart/order2.html', locals())


# 订单提交
@transaction.atomic
def order_handle(request):
    goods_ids = post(request, 'goods_ids').split(',')
    pay = post(request, 'pay')
    user_id = get_session(request, 'uid')

    # 获取购物车商品信息
    carts = GoodsCart.objects.filter(cart_user_id=user_id, cart_goods_id__in=goods_ids)

    # 获取用户
    user = User.objects.get(id=user_id)
    # 创建一个保存点
    save_point = transaction.savepoint()
    try:
        # 创建订单基本信息
        order = Order()
        order.order_user = user
        # 订单编号（用户ID + 时间戳 + 随机值）
        order.order_number = str(user_id) + str(int(time.time())) + str(random.randint(1000, 9999))
        order.order_tele = user.user_cellphone
        order.order_recv = user.user_name
        order.order_addr = user.user_addr
        order.order_pay = pay
        order.save()

        # 创建订单商品详情
        print(carts)
        if len(carts) == 0:
            # 数据为空，抛出异常。
            raise Exception
        for cart in carts:
            gd = Order_GoodsDetails()
            gd.goods_name = cart.cart_goods.good_name
            gd.goods_price = cart.cart_goods.good_price
            gd.goods_image = cart.cart_goods.good_image
            gd.goods_unit = cart.cart_goods.good_unit
            gd.goods_num = cart.cart_amount
            gd.goods_order = order
            gd.save()

        # 没有出错，删除购物车中已经提交的商品
        carts.delete()
        # 没有出错，提交事物
        transaction.savepoint_commit(save_point)

    except:
        # 如果操作出错，滚回保存点
        transaction.savepoint_rollback(save_point)
        return JsonResponse({'ret': 0})
    return JsonResponse({'ret': 1})



