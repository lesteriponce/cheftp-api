from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import ContactRequest
from .serializers import ContactRequestSerializer

class ContactRequestCreateView(APIView):

    @extend_schema(
        request=ContactRequestSerializer,
        responses={201: ContactRequestSerializer},
        description="Submit a Contact Us form request"
    )
    def post(self, request):
        serializer = ContactRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Your message has been received. We will get back to you shortly."},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ContactRequestListView(generics.ListAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

class ContactRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer