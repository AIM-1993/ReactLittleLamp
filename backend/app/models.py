from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
