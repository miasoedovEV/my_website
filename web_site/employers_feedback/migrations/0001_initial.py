# Generated by Django 3.2.6 on 2021-08-09 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='компания')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('text', models.CharField(max_length=1000, verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'отклик',
                'verbose_name_plural': 'отклики',
                'db_table': 'feedback',
            },
        ),
    ]
