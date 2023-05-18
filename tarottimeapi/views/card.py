from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tarottimeapi.models import Card

class CardView(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            card = Card.objects.get(pk=pk)
            serializer = CardSerializer(card, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(
            cards, many=True, context={'request': request})
        return Response(serializer.data)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'type', 'name_short', 'name', 'meaning_up', 'meaning_rev', 'desc', 'suit')
        depth = 1
