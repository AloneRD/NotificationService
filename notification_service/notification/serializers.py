from statistics import mode
from rest_framework import serializers
from .models import MailingList, Client, Message


class MailingListSerializer(serializers.ModelSerializer):
    model = MailingList
    fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    model = Client
    fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    model = Message
    fields = "__all__"
