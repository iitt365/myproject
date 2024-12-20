
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from myapp.models import UserProfile

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        email = data.get('email')

        # 检查是否已存在用户
        if UserProfile.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': '用户名已存在'})

        # 创建用户
        UserProfile.objects.create(username=username, email=email)
        return JsonResponse({'success': True, 'message': '注册成功'})

    return JsonResponse({'success': False, 'message': '无效的请求'})


def register_login_page(request):
    return render(request, 'register_login.html')




@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        remember_me = data.get('remember_me')

        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return JsonResponse({'success': False, 'message': '用户不存在'})

        # 创建会话
        request.session['user_id'] = user.id
        request.session['username'] = user.username

        # 如果选择了“记住我”，设置会话过期时间为两周
        if remember_me:
            request.session.set_expiry(1209600)  # 两周时间

        return JsonResponse({'success': True, 'message': '登录成功'})

    return JsonResponse({'success': False, 'message': '无效的请求'})
