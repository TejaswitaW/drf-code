from rest_framework.pagination import PageNumberPagination

class MyPage(PageNumberPagination):
    page_size = 1
    page_query_param = 'mypage'
    # client can give number of records(page size) to
    # view per page by using foll. attribute
    page_size_query_param = "myrecord"
    # to restric abuse of above feature
    max_page_size = 2
    last_page_strings = 'end'