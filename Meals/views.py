from django.db.models import Sum, F, ExpressionWrapper, IntegerField
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import meal
from .serializers import MealSerializer
from Bazar.models import Extra_Charge, Add_Cost

class MealViewSet(ModelViewSet):
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return meal.objects.select_related("member", "month")  # Optimization

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # Total meals
        total_sum = queryset.aggregate(
            total_all=Sum(
                ExpressionWrapper(F('lunch') + F('dinner') + F('is_guest'), output_field=IntegerField())
            )
        )
        total_meals = total_sum['total_all'] or 0

        # Total costs
        total_cost = Add_Cost.objects.aggregate(total_all_cost=Sum('meal_cost'))['total_all_cost'] or 0
        total_extra = Extra_Charge.objects.aggregate(extra_cost=Sum('extra_charge'))['extra_cost'] or 0

        # Grand total per meal
        grand_total = (total_cost + total_extra) / total_meals if total_meals > 0 else 0

        response = {
            "results": data,
            "total_cost": total_cost,
            "total_extra": total_extra,
            "total_all_meals": total_meals,
            "grand_total": grand_total
        }

        return Response(response)