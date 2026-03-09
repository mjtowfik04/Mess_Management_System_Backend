from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from django.db.models import Sum, F, ExpressionWrapper, IntegerField
from Bazar.models import Extra_Charge, Add_Cost
from Meals.models import meal


class UserSerializer(BaseUserSerializer):
    total_deposit = serializers.SerializerMethodField()
    total_meal = serializers.SerializerMethodField()
    meal_cost = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'total_deposit',
            'total_meal',
            'meal_cost',
            'balance'
        ]

    def get_total_deposit(self, obj):
        return obj.deposits.aggregate(
            total=Sum('deposit_amount')
        )['total'] or 0

    def get_total_meal(self, obj):
        total = obj.meals.aggregate(
            total=Sum(
                ExpressionWrapper(
                    F('lunch') + F('dinner') + F('is_guest'),
                    output_field=IntegerField()
                )
            )
        )['total'] or 0
        return total

    def get_meal_rate(self):
        total_meals = meal.objects.aggregate(
            total=Sum(
                ExpressionWrapper(
                    F('lunch') + F('dinner') + F('is_guest'),
                    output_field=IntegerField()
                )
            )
        )['total'] or 0

        total_cost = Add_Cost.objects.aggregate(
            total=Sum('meal_cost')
        )['total'] or 0

        total_extra = Extra_Charge.objects.aggregate(
            total=Sum('extra_charge')
        )['total'] or 0

        if total_meals == 0:
            return 0

        return (total_cost + total_extra) / total_meals

    def get_meal_cost(self, obj):
        meal_rate = self.get_meal_rate()
        total_meal = self.get_total_meal(obj)

        return total_meal * meal_rate

    def get_balance(self, obj):
        deposit = self.get_total_deposit(obj)
        meal_cost = self.get_meal_cost(obj)

        return deposit - meal_cost


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 'first_name', 'last_name']

    