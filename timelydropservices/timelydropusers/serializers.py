from rest_framework import serializers
from .models import User, PackageDelivery, GetAQuote, NewsletterSubscription, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PackageDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageDelivery
        fields = '__all__'
        read_only_fields = ('tracking_number', 'created_at', 'updated_at')


class GetAQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetAQuote
        fields = '__all__'
        read_only_fields = ('is_quote_accepted')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'email', 'review_text', 'created_at']
        read_only_fields = ('created_at',)


class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = '__all__'
