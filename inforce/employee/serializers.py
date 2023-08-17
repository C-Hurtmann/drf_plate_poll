from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Vote
        fields = ('user', 'menu')
        read_only_fields = ('user',)