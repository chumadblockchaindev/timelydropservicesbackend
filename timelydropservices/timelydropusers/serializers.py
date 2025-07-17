from rest_framework import serializers
from .models import User, PackageDelivery, GetAQuote, NewsletterSubscription


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
        read_only_fields = ('is_quote_accepted',)


class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = '__all__'
