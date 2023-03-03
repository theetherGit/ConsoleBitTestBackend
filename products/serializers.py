from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("The name field is required.")

        if data.get('price') and data.get('price') <= 0:
            raise serializers.ValidationError("The price must be greater than zero.")

        return data
