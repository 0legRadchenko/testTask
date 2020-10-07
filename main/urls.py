from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('companies', CompanyViewSet, basename='companies_here')
urlpatterns = router.urls

urlpatterns += [
    path("all-profiles/", UserProfileListView.as_view(), name="all-profiles"),
    path("profile/<int:pk>/", UserProfileDetailView.as_view(), name="profile"),
]