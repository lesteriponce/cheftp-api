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
        read_only_fields = ['id', 'status', 'created_at']
