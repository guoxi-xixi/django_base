from django.urls import path, register_converter
from book.views import create_book, shop, register, json, method, mobilePhone, response
from book.views import *
from django.urls import converters

class MobileCoverters():
    # 验证数据的正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据，给视图函数
    def to_python(self, value):
        return value

    # def to_url(self, value):
    # 将匹配结果用于反向解析传值时使用（了解）
    #     return str(value)

# 先注册转换器，才能在视图中使用
# converter 转换器类
# type_name 转换器名字
register_converter(MobileCoverters, 'phone')

urlpatterns = [
    path('create/', create_book),
    # <转换器名字：变量名>
    # 转换器会对变量数据进行 正则校验
    path('<int:city_id>/<int:shop_id>', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
    path('phone:phone_number/', mobilePhone),
    path('response/', response),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
]
