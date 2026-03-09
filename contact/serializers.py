from rest_framework import serializers
from .models import ContactRequest

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = [
            'id',
            'full_name',
            'email',
            'phone_number',
            'address',
            'date_requested',
            'message',
            'status',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'full_name': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False},
            'phone_number': {'required': True, 'allow_blank': False},
            'address': {'required': True, 'allow_blank': False},
            'message': {'required': True, 'allow_blank': False},
            'date_requested': {'required': True},
        }
