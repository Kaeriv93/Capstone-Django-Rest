from django.urls import include, path
from rest_framework import routers
from .views import UserDetailAPI, RegisterUserAPIView
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomerUserViewSet)
router.register(r'blog', views.BlogViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('get-details', UserDetailAPI.as_view()),
    path('register', RegisterUserAPIView.as_view()),
]