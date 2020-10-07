from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from .models import *
from .permissions import IsOwnerProfileOrReadOnly
from time import time
from .service import ProductFilter
from rest_framework.filters import SearchFilter
from rest_framework import generics, permissions, viewsets
from .mixins import MixedPermissionModelViewSet
from django.contrib.gis.db.models.functions import GeometryDistance
from django_filters.rest_framework import DjangoFilterBackend


l = ['create', 'destroy', 'partial_update', 'update']
DICT_WITH_PERMISSIONS = {k: [IsAuthenticated] for k in l}


class CategoryViewSet(MixedPermissionModelViewSet, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes_by_action = DICT_WITH_PERMISSIONS

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CategoryDetailSerializer
        else:
            return CategorySerializer


class CompanyViewSet(MixedPermissionModelViewSet, viewsets.ModelViewSet):
    permission_classes_by_action = DICT_WITH_PERMISSIONS
    model = Company

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CompanyDetailSerializer
        else:
            return CompanySerializer

    def get_queryset(self):
        location1 = None
        try:
            user = self.request.user.profile
            location1 = user.user_location
        except:
            print('NO USER')

        if location1 is None:
            queryset = Company.objects.filter(is_active=1)
        else:
            queryset = Company.objects.annotate(distance=GeometryDistance("location", location1)).order_by("distance")
        return queryset


class ProductViewSet(MixedPermissionModelViewSet, viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=1)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['title', 'description']
    filterset_class = ProductFilter
    permission_classes_by_action = DICT_WITH_PERMISSIONS

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        else:
            return ProductSerializer


class UserProfileListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]



