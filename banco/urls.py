from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('list-bank', views.ListBankViewSet, basename='list-banks')
router.register('register-bank', views.BanksUsersViewSet, basename='register-bank')

urlpatterns = router.urls
