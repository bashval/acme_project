from django.db import models
from django.urls import reverse

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
        validators=(real_age,)
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='birthdays_images',
        blank=True,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_mane', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def get_absolute_url(self):
        return reverse("birthday:detail", kwargs={"pk": self.pk})
