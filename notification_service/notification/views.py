import json
from .models import MailingList, Client, Message
from .serializers import MailingListSerializer, ClientSerializer, MessageSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count


class MailingListViewSet(viewsets.ModelViewSet):
    serializer_class = MailingListSerializer
    queryset = MailingList.objects.all()

    @action(detail=False)
    def get_total_stats(self, request):
        total_mailing_list = MailingList.objects.count()
        messages_no_sent, messages_sent = Message.objects.all().values('status').annotate(total=Count('status'))
        content = {
            "Общее колличество рассылок": total_mailing_list,
            "Колличество отправленных сообщений": messages_sent['total'],
            "Колличество не отправленных сообщений": messages_no_sent['total']
            }
        return Response(content)


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
