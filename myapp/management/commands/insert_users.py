from django.core.management.base import BaseCommand
from myapp.models import UserProfile
from django.utils import timezone
from faker import Faker

class Command(BaseCommand):
    help = 'Insert or update 10 random user profiles into the UserProfile model.'

    def handle(self, *args, **kwargs):
        fake = Faker()  # 初始化 Faker
        users = []

        for _ in range(10):  # 生成 10 个随机用户
            users.append({
                'username': fake.first_name(),  # 随机生成英文名字
                'email': fake.email(),         # 随机生成电子邮件
            })

        for user_data in users:
            username = user_data.pop('username')  # 提取用户名作为查询条件
            UserProfile.objects.update_or_create(
                username=username,  # 查找依据
                defaults=user_data  # 如果存在，则更新这些字段
            )

        self.stdout.write(self.style.SUCCESS('Successfully inserted or updated 10 random user profiles.'))
