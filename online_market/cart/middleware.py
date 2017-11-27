from .models import *
from utils.wrappers import *


class RecordCartsMiddleware(object):
    def process_request(self, request):
        uid = get_session(request, 'uid')
        request.total = 0
        request.money = 0
        if uid:
            # 把每个用户的购物车产品数量和总价添加到request上
            carts = GoodsCart.objects.filter(cart_user_id=get_session(request, 'uid'))
            for cart in carts:
                request.total += cart.cart_amount
                request.money += cart.cart_goods.good_price*cart.cart_amount