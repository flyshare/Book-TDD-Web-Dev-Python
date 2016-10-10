from django.db import models

class List(models.Model):
    pass

class Item(models.Model):
    """
    继承自 models.Model 的类 映射到数据库中的一个表
    默认情况,ID 字段会自动生成,其他字段需要手动添加
    """
    text = models.TextField(default='')
    # 让 Item 的list 字段的类型 跟 List() 对象 关联起来 这里就不是单纯的 text 类型了
    list = models.ForeignKey(List, default=None)



