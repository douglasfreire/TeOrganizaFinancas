from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('register-income', views.IncomeViewSet, basename='register-income')

urlpatterns = router.urls
