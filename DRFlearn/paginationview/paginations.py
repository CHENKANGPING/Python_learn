from rest_framework.pagination import PageNumberPagination

class MerchantPageNumberPagination(PageNumberPagination):
    # 默认一页的大小
    page_size = 5
    # 每页最多不能超过30条数据
    max_page_size = 10
    # 用户自己指定一页展示多少条数据
    page_size_query_param = 'size'
