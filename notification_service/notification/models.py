import pytz
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MailingList(models.Model):
    date_time_start = models.DateTimeField(verbose_name='дата и время начала')
    message_text = models.TextField(verbose_name='текст сообщение')
    tag = models.CharField(max_length=100, db_index=True, verbose_name='тег')
    date_time_finish = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='дата и время окончания'
        )

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


class Message(models.Model):
    STATUS = [
        ('SENT', 'Sent'),
        ('NO SENT', 'No sent')
    ]
    date_time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата и время отправки сообщения'
        )
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        verbose_name='статус отправки'
        )
    mailing = models.ForeignKey(
        MailingList,
        on_delete=models.CASCADE,
        related_name='messages'
        )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='messages'
        )

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return f'Сообщение {self.id} клиенту {self.client} '
