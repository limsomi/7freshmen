from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Profile(models.Model):

    GENDER_CHOICES = {
        ('male','남성'),
        ('female','여성'),
    }

    MBTI_CHOICES = {
        ('ESTJ','ESTJ'),
        ('ESTP','ESTP'),
        ('ESFJ','ESFJ'),
        ('ESFP','ESFP'),
        ('ENTJ','ENTJ'),
        ('ENTP','ENTP'),
        ('ENFJ','ENFJ'),
        ('ENFP','ENFP'),
        ('ISTJ','ISTJ'),
        ('ISTP','ISTP'),
        ('ISFJ','ISFJ'),
        ('ISFP','ISFP'),
        ('INTJ','INTJ'),
        ('INTP','INTP'),
        ('INFJ','INFJ'),
        ('INFP','INFP'),
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=128, null=True, blank=False)
    major = models.CharField(max_length=128, null=True, blank=False)
    gender = models.CharField(max_length=16, choices=GENDER_CHOICES, null=True)
    mbti = models.CharField(max_length=16, choices=MBTI_CHOICES, null=True)
    age = models.IntegerField(null=True)

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save,sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()