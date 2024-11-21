from django.db import models
from django.contrib.auth.models import AbstractUser

class users(AbstractUser):
    bal=models.IntegerField(default=0)


class post(models.Model):
    title=models.CharField(max_length=200)
    problem=models.TextField()
    user=models.ForeignKey(users,on_delete=models.CASCADE, null=True,blank=True,)

    def __str__(self):
        return self.title


class comment(models.Model):
    answer=models.TextField()
    user=models.ForeignKey(users,on_delete=models.CASCADE, null=True,blank=True,)
    post=models.ForeignKey(post,on_delete=models.CASCADE, null=True,blank=True,)


    def __str__(self):
        return self.answer



# Create your models here.
