from rest_framework.pagination import CursorPagination

class MyPage(CursorPagination):
    page_size = 1
    # instead of defualt created ordering
    # we are ordering by name
    ordering = 'name'
    