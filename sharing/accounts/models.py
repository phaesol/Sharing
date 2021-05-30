from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pk = models.IntegerField(blank=True)
    email = models.EmailField(max_length=200, blank=True)
    mygit = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    # 유저가 해당 프로필의 이미지를 등록하지 않으면 default 이미지 사용. 해당 프로필 이미지는 업로드시 자동으로 media/profile/image 에 담김.
    photo = models.ImageField(upload_to="profile/image", default='user.png')
    myInfo = models.CharField(max_length=150, blank=True)

#User 모델의 인스턴스가 저장될 때만 해당 메소드 호출.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()