# Generated by Django 3.1.14 on 2022-03-04 18:10

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number must be digits only.', regex='^\\+?1?\\d{9,18}$')]),
        ),
    ]
