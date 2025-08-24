from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    recipient_username = serializers.CharField(source='recipient.username', read_only=True)
    target_object_type = serializers.SerializerMethodField()
    target_object_id = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id',
            'actor',
            'actor_username',
            'recipient',
            'recipient_username',
            'verb',
            'target_object_type',
            'target_object_id',
            'timestamp',
            'is_read',
        ]
        read_only_fields = ['id', 'timestamp', 'actor_username', 'recipient_username']

    def get_target_object_type(self, obj):
        if obj.target:
            return obj.target._meta.model_name
        return None

    def get_target_object_id(self, obj):
        if obj.target:
            return obj.target.id
        return None
