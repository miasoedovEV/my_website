from django.core.validators import RegexValidator
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='компания')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='номер телефона')  # validators should be a list
    email = models.EmailField(verbose_name='ваша электронная почта')
    text = models.TextField(max_length=1000, verbose_name='сопроводительное письмо')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'feedback'
        verbose_name = 'отклик'
        verbose_name_plural = 'отклики'

# Create your models here.
