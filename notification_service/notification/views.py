from .models import MailingList, Client, Message
from rest_framework import viewsets


class MailingListViewSet(viewsets.ModelViewSet):
    model = MailingList
    queryset = MailingList.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    model = Client
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    model = Message
    queryset = Message.objects.all()
