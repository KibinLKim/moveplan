# Generated by Django 2.2.6 on 2019-11-08 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='retirecalculate',
            name='RetireExpected',
            field=models.CharField(default='example', max_length=255),
        ),
    ]