from django.db import models


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
