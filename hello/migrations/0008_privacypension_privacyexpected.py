# Generated by Django 2.2.6 on 2019-11-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20191117_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypension',
            name='PrivacyExpected',
            field=models.CharField(default='example', max_length=255),
        ),
    ]
