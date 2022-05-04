from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare(MiddlewareMixin):

    def process_request(self, request):

        print('111111111111 每次请求前都会执行')

    def process_response(self, request, response):

        print('每次响应钱都会执行 11111111111111111111')

        return response


class TestMiddleWare2(MiddlewareMixin):

    def process_request(self, request):
        print('22222222222222 每次请求前都会执行')

    def process_response(self, request, response):
        print('每次响应钱都会执行 2222222222222222')

        return response