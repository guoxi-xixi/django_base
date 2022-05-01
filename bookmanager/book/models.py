from django.db import models

# Create your models here.
"""
1. 我们的模型类 需要继承自 models.Model
2. 系统会自动为我们添加一个主键--id
3. 字段
    
    字段名=model.类型（选项）
    
    字段名其实就是数据表的字段名
    字段名不要使用 python，mysql等关键字
    
    char（M）
    varchar(M)
    M 就是选项
"""

# 书籍列表类型
class BookInfo(models.Model):
    # 创建字段，字段类型
    name = models.CharField(max_length=10)

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name

# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)