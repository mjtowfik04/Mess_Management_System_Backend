from django.urls import path, include

from rest_framework.routers import DefaultRouter
from Meals.views import MealViewSet

from Billing.views import monthViewsSet,AddMemberMoneyViewSet
from Bazar.views import AddCostViewSet,ExtraChargeViweSet


router = DefaultRouter()
# meal
router.register('meals', MealViewSet, basename='meals')
router.register('month', monthViewsSet, basename='month')

# Billing
router.register('addmoney',AddMemberMoneyViewSet,basename='addmoney')

# Bazer
router.register('addcost',AddCostViewSet,'addcost')
router.register('extracost',ExtraChargeViweSet,'extracost')


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]