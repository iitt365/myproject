from django.urls import path
from . import views

app_name = 'myauth'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register_login/', views.register_login_page, name='register_login'),
]
