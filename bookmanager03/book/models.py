from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name='书籍名称')
    pub_date = models.DateField(null=True, verbose_name='发布日期')
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta():
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    """准备人物列表信息的模型类"""

    # 定义性别的有序字典
    GENDER_CHIOCE = (
        (0, 'male'),
        (1, 'female')
    )

    name = models.CharField(max_length=10, unique=True, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=GENDER_CHIOCE, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')

    class Meta():
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
