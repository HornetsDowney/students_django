from django.db import models


# Create your models here.

# 创建用户表
class students(models.Model):
    student_user = models.CharField(max_length=20, unique=True)
    student_password = models.IntegerField(null=False)
    student_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.student_name
