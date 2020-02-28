from rest_framework import serializers

from api.models import Attacks


class AttacksSerializer(serializers.ModelSerializer):
    # status = serializers.SerializerMethodField()

    class Meta:
        model = Attacks
        fields = '__all__'
