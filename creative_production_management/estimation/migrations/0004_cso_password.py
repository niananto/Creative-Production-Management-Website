# Generated by Django 4.1.7 on 2023-02-22 07:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimation', '0003_alter_vendor_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso',
            name='password',
            field=models.CharField(default=12345678, max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z0-9]{8,}$')], verbose_name='password'),
            preserve_default=False,
        ),
    ]
