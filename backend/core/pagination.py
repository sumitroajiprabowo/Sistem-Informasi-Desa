from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    page_size = 5


class MediumSetPagination(PageNumberPagination):
    page_size = 30


class LargeSetPagination(PageNumberPagination):
    page_size = 50
