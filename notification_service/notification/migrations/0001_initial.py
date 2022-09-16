# Generated by Django 4.1.1 on 2022-09-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_start', models.DateTimeField(verbose_name='дата и время')),
                ('message', models.TextField(verbose_name='сообщение')),
                ('tag', models.CharField(db_index=True, max_length=100, verbose_name='тег')),
                ('date_time_finish', models.DateTimeField(verbose_name='дата и время')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
    ]