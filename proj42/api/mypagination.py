from rest_framework.pagination import LimitOffsetPagination

class MyPage(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = "mylimit"
    max_limit = 1
    