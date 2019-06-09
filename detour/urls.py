from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('collections/', views.CollectionList.as_view(), name='collection_list'),
    path('collections/<int:pk>', views.CollectionDetail.as_view(),
         name='collection_detail'),
    path('favorites/', views.FavoriteList.as_view(), name='favorite_list'),
    path('favorites/<int:pk>', views.FavoriteDetail.as_view(), name='favorite_detail')
]
