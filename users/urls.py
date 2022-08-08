
from django.urls import  re_path, path, include
from . import views

from users import views
urlpatterns = [
    
    
    path('create_user/', views.CreateUser.as_view(), name="create_user"),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
]