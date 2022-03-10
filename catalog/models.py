from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ['male', u"Мужской"],
    ['female', u"Женский"],
]


class Profile(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=u"Имя")
    last_name = models.CharField(max_length=100, verbose_name=u"Фамилия")
    avatar = models.FileField(null=True, blank=True, verbose_name=u"Аватар")
    email = models.CharField(max_length=100, verbose_name=u"E-mail")
    gender = models.CharField(max_length=10, verbose_name=u"Пол", choices=GENDER_CHOICES, default="male")
