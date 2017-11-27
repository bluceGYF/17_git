from django.db import models
from db.AbstractModel import *
from utils.wrappers import *
from tinymce.models import HTMLField


# 用户模型管理类
class UserManager(models.Manager):
    # 根据用户名查询用户数据
    def user_by_user_name(self, username):
        try:
            return self.get(user_name=username)
        except User.DoesNotExist:
            return None

    def user_register_save(self, request):
        # 创建user对象
        user = User()
        user.user_name = post(request, 'user_name')
        user.user_pass = password_encryption(post(request, 'pass1'))
        # 保存数据
        user.save()

    def user_addr_updata(self, request, user_addr):
        user = self.user_by_user_name(get_session(request, 'username'))
        user.user_true_name = post(request, 'true_name')
        user.user_card_id = post(request, 'id_card')
        user.user_code = post(request, 'code')
        user.user_cellphone = post(request, 'cell_phone')
        user.user_tele = post(request, 'tele')

        user.user_addr = user_addr + post(request, 'user_detail_addr')
        user.save()


# 定义用户数据模型
class User(AbstractModel):
    user_name = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=110)
    user_addr = models.CharField(max_length=100)
    user_tele = models.CharField(max_length=20)
    user_cellphone = models.CharField(max_length=11, default='')
    user_code = models.CharField(max_length=6)
    user_true_name = models.CharField(max_length=50)
    user_card_id = models.CharField(max_length=30)

    # 自定义管理器对象
    objects = UserManager()


# 省市联动
class CityInfo(models.Model):
    # 城市名字
    city_name = models.CharField(max_length=50)
    # 城市编码
    city_code = models.CharField(max_length=50)
    # 父级城市
    city_baba = models.CharField(max_length=50, null=True, blank=True)



