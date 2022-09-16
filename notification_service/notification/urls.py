from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notification import views


router = DefaultRouter()
router.register(r'mailing-list', views.MailingListViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'message', views.MessageViewSet)
print(router.urls)

urlpatterns = [
    path('v1/', include(router.urls))
]
