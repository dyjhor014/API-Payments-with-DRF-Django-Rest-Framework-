from rest_framework.routers import DefaultRouter
from payments.api.api import ServiceViewSet, PaymentUserViewSet

router = DefaultRouter()

router.register(r'services',ServiceViewSet,basename = 'services'),
router.register(r'payment_user',PaymentUserViewSet,basename = 'paymentusers'),
#router.register(r'expired_payment',ExpiredPaymentViewSet,basename = 'expiredpayments')

urlpatterns = router.urls