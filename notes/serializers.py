from rest_framework import serializers

from . import models


class NoteSerializer(serializers.Serializer):
    class Meta:
        model = models.Note
        fields = '__all__'

