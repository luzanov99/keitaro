
from django.urls import  re_path, path, include
from . import views
from rest_framework.routers import DefaultRouter
from users import views
from django.contrib.auth.views import LogoutView
router = DefaultRouter()

router.register('create_user', views.CreateUserViewSet, basename='user')
urlpatterns = [
    
    path('', include(router.urls)),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
]