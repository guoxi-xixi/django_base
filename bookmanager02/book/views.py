from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    return HttpResponse('index')

#####################增加数据############################
from book.models import BookInfo
# 方式一
book = BookInfo(
    name = 'Django',
    pub_date = '2020-1-1',
    readcount = 10
)
# 必须要调用 对象的save方法才能将数据保存到数据库中
book.save()


# 方式二
# objects -- 相当于一个代理 实现增删改查

BookInfo.objects.create(
    name='测试开发入门',
    pub_date='2020-10-10',
    readcount=100
)

#####################修改数据############################
# 方式一：
# select * from bookinfo where name='测试开发入门'

book = BookInfo.objects.get(name='测试开发入门')
book.name='python测开'

# 方式二：
# filter() 过滤
BookInfo.objects.filter(name='python测开').update(name='python测试开发入门')

# 错误方式
# BookInfo.objects.get(name='Django').update(name='Django入门')
# AttributeError: 'BookInfo' object has no attribute 'update'

#####################删除数据############################
# 方式一：
# 删除分2中， 物理删除（这条记录的数据 删除） 和 逻辑删除（修改标记位 例如 is_delete=False）

book = BookInfo.objects.get(name='python测试开发入门')
book.delete()

# 方式二：
BookInfo.objects.get(name='python测试开发入门').delete()
BookInfo.objects.filter(name='python测试开发入门').delete()

#####################查询数据############################

# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
# all查询多个结果。
# count查询结果数量。
try:
    book = BookInfo.objects.get(id=999)
except BookInfo.DoesNotExist:
    print("查询结果不存在")

# all查询多个结果
BookInfo.objects.all()
from book.models import PeopleInfo
PeopleInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()
PeopleInfo.objects.all().count()

#####################过滤查询############################

# 实现SQL中的where功能，包括
#
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

# 模型类名.objects.filter(属性名__运算符=值)       获取n个结果  n=0,1,2,...
# 模型类名.objects.exclude(属性名__运算符=值)      获取n个结果  n=0,1,2,...
# 模型类名.objects.get(属性名__运算符=值)          获取1个结果 或者 异常

# 查询编号为1的图书
book = BookInfo.objects.get(id=1)           # 简写形式 （属性名 = 值）
book = BookInfo.objects.get(id__exact=1)    #完整形式  (id__exact=1)

book = BookInfo.objects.get(pk=1)   # pk primary key 主键

BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5,7,9,11])

# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

######################### F & Q ################################
from django.db.models import F

# 使用： 2个属性的比较
#语法形式： 以filter 为例  模型类名.objects.filter(属性名__运算符=F('第二个属性名'))

# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount'))

# 可以在F对象上使用算数运算。查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)

# 并且查询
# 查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 或者
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

# 或者查询
# 查询阅读量大于20，或者编号小于3的图书。
from django.db.models import Q

# 或者语法：  模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|...)
# 并且语法：  模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&...)
# not 非 语法：  模型类名.objects.filter(～Q(属性名__运算符=值))

BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

# 查询编号不等于3的书籍
BookInfo.objects.exclude(id=3)

BookInfo.objects.filter(~Q(id=3))

######################### 聚合函数 ################################
from django.db.models import Sum,Avg,Max,Min,Count

# 模型类名.objects.aggregate(Xxx('字段名'))

BookInfo.objects.aggregate(Sum('readcount'))

######################### 排序函数 ################################

BookInfo.objects.all().order_by('readcount')    # 升序
BookInfo.objects.all().order_by('-readcount')    # 降序

######################### 2个表的级联操作 ################################

# 查询书籍为1的所有人物信息

book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()
# <QuerySet [<PeopleInfo: 郭靖>, <PeopleInfo: 黄蓉>, <PeopleInfo: 黄药师>, <PeopleInfo: 欧阳锋>, <PeopleInfo: 梅超风>]>

# PeopleInfo.objects.filter(book=1)
# <QuerySet [<PeopleInfo: 郭靖>, <PeopleInfo: 黄蓉>, <PeopleInfo: 黄药师>, <PeopleInfo: 欧阳锋>, <PeopleInfo: 梅超风>]>

# 查询人物为1的书籍信息
person = PeopleInfo.objects.get(id=1)
person.book.name    # '射雕英雄传'

######################### 关联过滤查询 ################################
# 语法形式
# 查询1的数据， 条件为 n
# 模型类名.objects.(关联模型类名小写__字段名__运算符=值)

# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name='郭靖')  #<QuerySet [<BookInfo: 射雕英雄传>]>
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')

# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')
# <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>

# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__name__exact='天龙八部')

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)
