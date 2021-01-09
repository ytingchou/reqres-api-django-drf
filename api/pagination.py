from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class ListPagination(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('per_page', self.page.paginator.per_page),
            ('total', self.page.paginator.count),
            ('total_pages', self.page.paginator.num_pages),
            ('data', data)
        ]))
