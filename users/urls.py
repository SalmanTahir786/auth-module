
from .views import RegisterAPI
from django.urls import path
# from rest_framework import routers

from knox import views as knox_views
from .views import LoginAPI, UpdateIsActiveAPIView

# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'api/is_active/<pk:int>/', UpdateIsActiveAPIView, 'is_active')

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/delete/<int:pk>/', UpdateIsActiveAPIView.as_view(), name='soft_delete_user'),
]

# urlpatterns += router.urls