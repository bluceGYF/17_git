from django.test import TestCase
from .models import *
import random


# cags = ['纸杯系列', '餐具系列', '运动系列']
# for cag in cags:
#     good_cag = Goods_category()
#     good_cag.cag_name = cag
#     good_cag.save()

# son_cags = ['纸碟', '纸袋', '纸碗', '食品袋', '厨房三件宝']
# for cag in son_cags:
#     good_son_cag = Goods_son_category()
#     good_son_cag.cag_name = cag
#     good_son_cag.cag_father_id = 3
#     good_son_cag.save()

# # 创建子分类
# son_cag = ['蛋糕', '沙拉', '西餐', '中餐', '外带打包']
#
# 创建测试数据
# with open('/home/python/Desktop/online_market/data2.txt', 'r') as f:
#     for name in f:
#         goods = GoodsInfo()
#         goods.good_name = name[:-1]
#         goods.good_unit = '袋'
#         goods.good_price = random.randint(10, 1000)
#         goods.good_size = '100ml'
#         goods.good_image = 'omkt_goods/' + str(random.randint(1, 5)) + '.jpg'
#         goods.good_desc = '这个产品来源于欧洲，规划中上海四大商业附中心—真如商业副中心，婚房精装电梯两房。让您一步到位很荣'
#         goods.good_code = random.randint(100000, 999999)
#         goods.good_cag_id = 3
#         goods.good_son_cag_id = random.randint(11, 15)
#         goods.save()



