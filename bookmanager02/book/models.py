from django.db import models

# Create your models here.
"""
1. 模型类 需要继承自 models.Model
2. 定义属性
    id 系统会默认生成
    属性名 = models.类型(选项)
    
    2.1 属性名 对应 字段名
        不要使用 python, MySQL 关键字
        不要使用连续下划线 __
    2.2 类型 MySQL 的类型
    2.3 选项 默认值，唯一键，是否为null
        CharField 必须设置max_length
        verbose_name 主要是 admin 站点使用
        
3. 改变表的名称
    默认表的名字是：子应用名_类型 -- 都是小写
    修改表的名字
    create table 'bool_info' (
        id int,
        name varchar(10) not null default ''
    )
"""

class BookInfo(models.Model):
    """准备书籍列表信息的模型类"""

    # 创建 BookInfo 表的字段和类型
    name = models.CharField(max_length=20, verbose_name='书籍名称')
    pub_date = models.DateField(null=True, verbose_name='发布日期')
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # 1对多的关系模型中
    # 系统会自动添加一个 关联模型类型 类名小写_set

    # pelpleinfo_set = [PeopleInfo,PeopleInfo, ...]
    # peopleinfo

    class Meta():
        db_table = 'bookinfo'   # 指明数据库表名
        verbose_name = '图书'    # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
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

    """
    外键：
        系统会自动为外键添加 _id
        外键的级联操作
            主表和从表
            1 对 多
            主表中的一条书籍删除量，从表的关联数据处理
            SET_NULL：设置为NULL，仅在该字段null=True允许为null时可用
            PROTECT：抛出异常不让删除
            CASCADE：级联删除
            
    """
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    # book = BookInfo()

    class Meta():
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name