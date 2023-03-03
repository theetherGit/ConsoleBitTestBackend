from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, pagination, filters
from rest_framework.permissions import IsAuthenticated

from products.filters import ProductFilter
from products.models import Product
from products.serializers import ProductSerializer


class ProductPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['name', 'price', 'created_at', 'updated_at']
    filterset_class = ProductFilter



