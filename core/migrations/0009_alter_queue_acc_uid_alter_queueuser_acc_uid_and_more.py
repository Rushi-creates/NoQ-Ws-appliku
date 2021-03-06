# Generated by Django 4.0.3 on 2022-06-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_authuser_options_alter_queue_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='acc_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authUser_in_queue_uid', to='core.authuser'),
        ),
        migrations.AlterField(
            model_name='queueuser',
            name='acc_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authUser_in_queueUser_uid', to='core.authuser'),
        ),
        migrations.AlterField(
            model_name='queueuser',
            name='q_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queue_in_QueueUser_uid', to='core.queue'),
        ),
    ]
