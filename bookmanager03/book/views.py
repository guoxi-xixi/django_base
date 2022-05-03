from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from book.models import BookInfo

# Create your views here.

################################# Request #######################################################################################################################################
def create_book(request):

    book = BookInfo.objects.create(
        name='abc',
        pub_date='2022-5-3',
        readcount=10
    )
    return HttpResponse('create')

def shop(request, city_id, shop_id):
    print(city_id,shop_id)

    query_params = request.GET
    print(query_params)
    # order = query_params['order']
    # order = query_params.get('oder')

    # <QueryDict: {'order': ['readcount'], 'page': ['1']}>
    # QueryDict 具有字典的特性
    # 还具有 一键多值
    #  # <QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']}>

    order = query_params.getlist('order')
    print(order)
    return HttpResponse('python_django学习')

def register(request):
    data = request.POST
    print(data)
    # < QueryDict: {'username': ['xixi'], 'password': ['123']} >

    return HttpResponse('Register')

def json(request):
    body = request.body
    # print(body)
    # b'{\n\t"name":"xixi",\n\t"age": 28\n}'

    body_str = body.decode()
    # print(body_str)
    """
    {
        "name":"xixi",
        "age": 28
    }
    
    <class 'str'>
    """
    # print(type(body_str))

    # JSON形式的字符串 可以转换为 Python的字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    # {'name': 'xixi', 'age': 28}

    ##############请求头############
    # print(request.META)
    print(request.META['SERVER_PROTOCOL'])

    return HttpResponse('json')

def method(request):
    print(request.method)

    return HttpResponse('method')

def mobilePhone(request, phone_number):

    print(phone_number)

    return HttpResponse('mobilePhone')

################################### Response #################################################
def response(request):

    # HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    # response = HttpResponse('res', status=200)
    #
    # response['name'] = 'xixi'
    #
    # return response

    # JSON -> dict
    # dict -> JSON

    info = {
        'name': 'xixi',
        'age': 28
    }
    info_list = [
        {
            'name': 'xixi',
            'age': 28
        },
        {
            'name': 'erxi',
            'age': 28
        }
    ]
    # response = JsonResponse(info)
    response = JsonResponse(info_list, safe=False)
    # response = JsonResponse(data=info_list, safe=False)
    # [{"name": "xixi", "age": 28}, {"name": "erxi", "age": 28}]

    return response
    # return redirect('http://www.baidu.com')

    # import json
    # data=json.dumps(info_list)
    #
    # response = HttpResponse(data)
    # return response

    # 1xx
    # 2xx
    #   200 成功
    # 3xx
    # 4xx   请求有问题
    #   404 找不到页面 路由有问题
    #   403 禁止访问    权限问题
    # 5xx
    # HTTP status code must be an integer from 100 to 599


#####################
"""
查询字符串

http://ip:port/path/path/?key=value&key1=value1

url 以 ？ 为分割 分为2部分
？前边为 请求路径
？后边为 查询字符串  查询字符串 类似于字典 key=value 多个数据采用&拼接


"""

########################### cookie和session ##############################################################################

"""
第一次请求，携带 查询字符串
http://127.0.0.1:8000/set_cookie/?username=zhangsan&password=123
服务器接收到请求之后，获取username.服务器设置cookie信息，cookie信息包括 username
浏览器接收到服务器的响应之后，应该把cookie保存起来


第二次及其之后的请求，我们访问http://127.0.0.1:8000 都会携带cookie信息。 服务器就可以读取cookie信息，来判断用户身份
"""
def set_cookie(request):
    # 设置cookies，服务器response设置cookie

    # 1.获取查询字符串数据
    username = request.GET.get('username')
    pwd = request.GET.get('pwd')

    # 2.服务器设置cookie
    response = HttpResponse('set_cookie')
    # key,value = ''    max_age 过期时间，秒
    response.set_cookie('name', username, max_age=3600) # 有效期一小时
    response.set_cookie('pwd', pwd) # 临时cookie
    # 删除cookies
    response.delete_cookie('pwd')

    return response

def get_cookie(request):
    # 获取cookies 从request中获取
    print(request.COOKIES)
    # request.COOKIES 是字典数据
    name = request.COOKIES.get('name')

    return HttpResponse(name)

################## session #####################
# session 是保存在服务器端 -- 数据相对安全
# session需要依赖于cookie

"""
第一次请求 http://127.0.0.1:8000/set_session/?username=zhangsan 。我们在服务器端设置sesison信息
服务器同时会生成一个sessionid的cookie信息。
浏览器接收到这个信息之后，会把cookie数据保存起来

第二次及其之后的请求 都会携带这个sessionid. 服务器会验证这个sessionid. 验证没有问题会读取相关数据。实现业务逻辑
"""

def set_session(request):

    # 1.模拟 获取用户信息
    username = request.GET.get('username')

    # 2. 设置session信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username

    # 删除session
    # request.session.clear() 清除 所有 session的value
    # request.session.clear()

    # request.session.flush() 清除 所有 session的 key&value
    # request.session.flush()

    # del request.session['键'] 清除 session 指定 key 的value
    # del request.session['48e4r7tydk1z8zs6rbvxk0ox1ti14zh2']

    # request.session.set_expiry(10)

    return HttpResponse('set_session')

def get_session(request):
    # 通过索引key 获取 字典 值，当session不存在/不匹配，异常报错，不推荐
    # user_id = request.session['user_id']
    # username = request.session['username']

    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{},{}'.format(user_id,username)

    return HttpResponse(content)