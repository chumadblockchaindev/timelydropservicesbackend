from django.db import models
import uuid
from django.core.mail import send_mail
from django.conf import settings

from_email = settings.DEFAULT_FROM_EMAIL  # or settings.EMAIL_HOST_USER


class User(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email


class PackageDelivery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package_type = models.CharField(max_length=50)
    delivery_date = models.DateTimeField(auto_now_add=True)
    pickup_address = models.CharField(max_length=100, blank=True)
    delivery_address = models.CharField(max_length=255)
    tracking_number = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    current_location = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delivered = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        is_update = self.pk is not None
        if not self.tracking_number:
            self.tracking_number = str(uuid.uuid4()).split("-")[0].upper()
        super().save(*args, **kwargs)

        # Automatically set is_delivered to True if status is 'delivered'
        if self.is_delivered or self.status == 'delivered':
            self.is_delivered = True
            self.current_location = self.delivery_address
            self.status = 'delivered'
            super().save(update_fields=['is_delivered'])

        # Send email if updated
        if is_update:
            subject = f'Update on Your Package Delivery - Tracking No: {self.tracking_number}'
            message = f'Hello {self.user.full_name}, \nYour delivery with tracking number {self.tracking_number} has been updated. \
                \nCurrent Location: {self.current_location} \
                \nDelivery Status: {'Delivered' if self.is_delivered else self.status} \
                \n\nThank you for chosing TimelyDropService!'
            send_mail(
                subject,
                message,
                from_email,  # From email
                [self.user.email],  # To email
                fail_silently=False)

    def __str__(self):
        return f"Delivery for {self.user.email} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')} - Status: {self.status}"


class GetAQuote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    carton_dimension = models.CharField(max_length=50)
    package_details = models.TextField()
    is_quote_accepted = models.BooleanField(default=False)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote for {self.email} - {'Accepted' if self.is_quote_accepted else 'Pending'}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.name} - {'Approved' if self.is_approved else 'Pending'}"


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
