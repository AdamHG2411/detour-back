from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('maps/', views.MapList.as_view(), name='map_list'),
    path('maps/<int:pk>', views.MapDetail.as_view(),
         name='map_detail'),
    path('detours/', views.DetourList.as_view(), name='detour_list'),
    path('detours/<int:pk>', views.DetourDetail.as_view(), name='detour_detail')
]
