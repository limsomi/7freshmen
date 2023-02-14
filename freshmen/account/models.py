from django.db import models

# Create your models here.

# 초기 회원가입 시 유저 모델
class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='아이디')
    user_name = models.CharField(max_length=32, unique=True, verbose_name='닉네임')
    user_pw = models.CharField(max_length=128, verbose_name='비밀번호')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'