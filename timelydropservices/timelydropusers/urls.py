from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PackageDeliveryViewSet, CreateQuoteView, CreateNewsletterSubscription, TrackDeliveryView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'deliveries', PackageDeliveryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_quote/', CreateQuoteView.as_view(), name='get-quote'),
    path('subscribe/', CreateNewsletterSubscription.as_view(),
         name='subscribe-newsletter'),
    path('track/<str:tracking_number>/',
         TrackDeliveryView.as_view(), name='track-delivery'),
]
