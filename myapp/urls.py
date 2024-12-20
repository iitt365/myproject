from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
path('table/', views.table_view, name='table_view'),
path('users/', views.user_list, name='user_list'),  # 用户列表视图
]
