from django.db import models


# 抽象基类
class AbstractModel(models.Model):
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 是否逻辑删除
    is_delete = models.BooleanField(default=False)

    # 设定该类为抽象基类
    class Meta:
        abstract = True
