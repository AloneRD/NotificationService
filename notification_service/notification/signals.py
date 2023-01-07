from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.models import MailingList, Client, Message


@receiver(post_save, sender=MailingList)
def create_message(sender, instance, created, **kwargs):
    clients = Client.objects.filter(tag=instance.tag)
    messages = [
        Message(
            status = 'NO SENT',
            mailing = instance,
            client = client
        ) for client in clients
    ]
    Message.objects.bulk_create(messages)
