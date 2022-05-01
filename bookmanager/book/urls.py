from django.urls import path

from book.views import index

# 这个是固定写法 urlpatterns = []
urlpatterns = [
    path('index/', index)
]