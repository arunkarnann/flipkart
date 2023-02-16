# urls.py for the app
from django.urls import path
from .views import ProductViewSet, Home, SearchViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include
router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns =[
    path('', include(router.urls)),
    path("home/", Home.as_view(), name="home"),
    path("search/", SearchViewSet.as_view({'get': 'list'}) , name="search")
]