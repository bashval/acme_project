from django.db import models

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20
    )
    last_mane = models.CharField(
        verbose_name='Фамилия',
        max_length=20,
        blank=True,
        help_text='Необязательное поле'
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        validators=(real_age,),
    )
