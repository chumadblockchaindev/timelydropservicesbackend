from django.contrib import admin
from .models import User, PackageDelivery, GetAQuote, NewsletterSubscription, Review


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone_number', 'location')
    search_fields = ('email', 'full_name')


@admin.register(PackageDelivery)
class PackageDeliveryAdmin(admin.ModelAdmin):
    list_display = ('user', 'package_type', 'delivery_date', 'status',
                    'tracking_number', 'created_at', 'updated_at', 'is_delivered')
    search_fields = ('user__email', 'package_type', 'status')


@admin.register(GetAQuote)
class GetAQuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'carton_dimension',
                    'package_details', 'is_quote_accepted', 'request_date')
    search_fields = ('email',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'review_text',
                    'created_at', 'is_approved')
    search_fields = ('email', 'name')
    list_filter = ('is_approved',)


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on')
    search_fields = ('email',)
