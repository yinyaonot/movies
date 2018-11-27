from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# class TUser(models.Model):
#     create_date = models.DateTimeField(blank=True, null=True)
#     expire_date = models.DateTimeField(blank=True, null=True)
#     is_vip = models.BigIntegerField()
#     email = models.CharField(max_length=255, blank=True, null=True)
#     username = models.CharField(max_length=255, blank=True, null=True)
#     passwd = models.CharField(max_length=255, blank=True, null=True)
#     is_manager = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_user'


class User(AbstractUser):
    expire_date = models.DateTimeField(blank=True, null=True)
    is_vip = models.BigIntegerField(null=True)
    is_manager = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11, unique=True)
    class Meta(AbstractUser.Meta):
        # managed = False
        db_table = 't_user'