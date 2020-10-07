from rest_framework import serializers
from .models import UserProfile
from .models import *
import json
from .service import PointField1


class CompanySerializer(serializers.ModelSerializer):
    location = PointField1()

    class Meta:
        model = Company
        exclude = ('is_active', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    company_info = serializers.SerializerMethodField(read_only=True)
    category_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        exclude = ('is_active', )

    def get_company_info(self, obj):
        company = obj.company
        serializer = CompanySerializer(company)
        return serializer.data

    def get_category_info(self, obj):
        category = obj.category
        serializer = CategorySerializer(category)
        return serializer.data


class ProductListSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        exclude = ('is_active', )


class CategoryDetailSerializer(serializers.ModelSerializer):
    products_of_this_category = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class CompanyDetailSerializer(serializers.ModelSerializer):
    company_products = ProductSerializer(many=True)
    location = PointField1()

    class Meta:
        model = Company
        exclude = ('is_active', )


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_location = PointField1()

    class Meta:
        model = UserProfile
        fields = '__all__'
