from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from django.contrib import admin
from .models import ContactRequest

class ContactRequestViewSet(SnippetViewSet):
    model = ContactRequest
    name = 'contact_requests'
    icon = 'mail'
    menu_label = 'Contact Requests'
    menu_order = 200
    list_display = ['full_name', 'email', 'phone_number', 'status', 'created_at']
    list_filter = {'status': ['exact']}
    search_fields = ['full_name', 'email']
    panels = [
        MultiFieldPanel([
            FieldRowPanel([
            FieldPanel('full_name'),
            FieldPanel('email'),
            ]),
            FieldRowPanel([
            FieldPanel('phone_number'),
            FieldPanel('address'),
            ]),
            FieldPanel('date_requested'),
            FieldPanel('message'),
            FieldPanel('status'),
        ], heading='Contact Request Details'),
    ]

register_snippet(ContactRequest, viewset=ContactRequestViewSet)

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'email', 'phone_number', 'status', 'created_at']
    list_filter   = ['status']
    search_fields = ['full_name', 'email']
    ordering      = ['-created_at']