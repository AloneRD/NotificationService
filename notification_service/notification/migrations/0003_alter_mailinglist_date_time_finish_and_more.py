# Generated by Django 4.1.1 on 2022-09-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_client_remove_mailinglist_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='date_time_finish',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата и время окончания'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='date_time_start',
            field=models.DateTimeField(verbose_name='дата и время начала'),
        ),
    ]