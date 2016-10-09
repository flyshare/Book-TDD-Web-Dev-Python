from django.db import models


class Item(models.Model):
    """
    继承自 models.Model 的类 映射到数据库中的一个表
    默认情况,ID 字段会自动生成,其他字段需要手动添加
    """
    text = models.TextField(default='')
