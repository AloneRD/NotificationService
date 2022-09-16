import pytz
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MailingList(models.Model):
    date_time_start = models.DateTimeField(verbose_name='дата и время')
    message = models.TextField(verbose_name='сообщение')
    tag = models.CharField(max_length=100, db_index=True, verbose_name='тег')
    date_time_finish = models.DateTimeField(verbose_name='дата и время')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def __str__(self):
        return f'Рассылка {self.id}'


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phonenumber = PhoneNumberField(verbose_name='номер телефона')
    tag = models.CharField(
        max_length=100,
        db_index=True,
        blank=True,
        verbose_name='тег'
        )
    timezone = models.CharField(
        max_length=35,
        choices=TIMEZONES,
        verbose_name='часовой пояс'
        )

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f'Клиент {self.id}'
