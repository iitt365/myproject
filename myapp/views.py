from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings  # 导入settings模块
from .models import UserProfile

def index(request):
    return HttpResponse("Hello, Django project setup is successful!")

def table_view(request):
    # 使用settings.STATIC_URL来构建正确的静态文件路径
    image_dir = os.path.join(settings.STATIC_ROOT, 'myapp', 'images')
    images = os.listdir(image_dir)  # 获取图片文件的列表

    # 示例数据
    data = [
        {'id': 1, 'name': 'Item 1', 'value': 'Value 1'},
        {'id': 2, 'name': 'Item 2', 'value': 'Value 2'},
        # 更多数据...
    ]
    return render(request, 'table.html', {'images': images, 'data': data})

def user_list(request):
    # 获取所有用户
    users = UserProfile.objects.all()

    # 控制台输出：输出查询到的用户数据
    print("查询到的用户数据：")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

    # 渲染模板
    return render(request, 'user_list.html', {'users': users})
