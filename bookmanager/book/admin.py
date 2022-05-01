from django.contrib import admin

# Register your models here.
from book.models import BookInfo,PeopleInfo
# 注册后台管理模块
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)