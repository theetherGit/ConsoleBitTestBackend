import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    created_at_lte = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    created_at_gte = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    name_have = django_filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['name', 'name_have', 'description', 'min_price', 'max_price', 'created_at_lte']


