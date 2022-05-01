from django.db import models

# Create your models here.
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