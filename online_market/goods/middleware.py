from .models import *


# 给用户request绑定一个cags
class RecordCagsMiddleware(object):
    def process_request(self, request):
        # 把cags添加到request.cags属性上面
        cags = Goods_category.objects.all()
        request.cags = cags
