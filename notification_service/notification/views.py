from .models import MailingList, Client, Message
from .serializers import MailingListSerializer, ClientSerializer, MessageSerializer
from rest_framework import viewsets


class MailingListViewSet(viewsets.ModelViewSet):
    serializer_class = MailingListSerializer
    queryset = MailingList.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
