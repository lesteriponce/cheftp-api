from django.urls import path
from .views import (
    ContactRequestCreateView,
    ContactRequestListView,
    ContactRequestDetailView,
)

urlpatterns = [
    path('contact/', ContactRequestCreateView.as_view(), name='contact-request'),
    path('contact/list/', ContactRequestListView.as_view(), name='contact-list'),
    path('contact/<int:pk>/', ContactRequestDetailView.as_view(), name='contact-detail'),
]
