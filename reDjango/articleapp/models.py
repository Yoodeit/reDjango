from django.contrib.auth.models import User
from django.db import models
from projectapp.models import Project

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    # 유저가 지워지면 (알수없음) 이런식으로 뜨도록 하는 세팅이 SET_NULL, related name은 유저객체에서 접근하기 쉬우라고
    title = models.CharField(max_length=200, null=True)
    # 제목은 캐릭터필드. 최대길이 200에 null 허용
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)

    

