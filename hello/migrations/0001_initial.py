# Generated by Django 2.2.6 on 2019-11-08 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RetireCalculate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ThreeMonthCost', models.IntegerField()),
                ('YearPerformance', models.IntegerField()),
                ('YearAllowance', models.IntegerField()),
                ('WorkDays', models.IntegerField()),
            ],
        ),
    ]