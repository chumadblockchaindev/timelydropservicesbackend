from rest_framework import viewsets, generics, permissions
from .models import User, PackageDelivery, GetAQuote, NewsletterSubscription, Review
from .serializers import UserSerializer, PackageDeliverySerializer, GetAQuoteSerializer, NewsletterSubscriptionSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.serializers import ValidationError


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class PackageDeliveryViewSet(viewsets.ModelViewSet):
    queryset = PackageDelivery.objects.all()
    serializer_class = PackageDeliverySerializer
    permission_classes = [permissions.IsAdminUser]


class CreateQuoteView(generics.CreateAPIView):
    queryset = GetAQuote.objects.all()
    serializer_class = GetAQuoteSerializer


class CreateNewsletterSubscription(generics.CreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer


class TrackDeliveryView(generics.RetrieveAPIView):
    queryset = PackageDelivery.objects.all()
    serializer_class = PackageDeliverySerializer
    lookup_field = 'tracking_number'


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(is_approved=True)
