# Generated by Django 4.0.3 on 2022-06-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_queueuser_acc_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='queueuser',
            name='shop_name',
            field=models.CharField(default='no value', max_length=80),
        ),
    ]