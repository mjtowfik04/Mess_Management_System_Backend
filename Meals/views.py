from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Sum, F, ExpressionWrapper, IntegerField
from .models import meal
from .serializers import MealSerializer
from Bazar.models import Extra_Charge, Add_Cost
from api.permissions import IsStaffOrReadOnly
from api.paginations import DefaultPagination

class MealViewSet(ModelViewSet):
    pagination_class = DefaultPagination
    serializer_class = MealSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        return meal.objects.select_related("member", "month")  

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Pagination apply
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            paginated_response = Response(serializer.data)

        # Extra aggregates
        total_sum = queryset.aggregate(
            total_all=Sum(
                ExpressionWrapper(F('lunch') + F('dinner') + F('is_guest'), output_field=IntegerField())
            )
        )
        total_meals = total_sum['total_all'] or 0

        total_cost = Add_Cost.objects.aggregate(total_all_cost=Sum('meal_cost'))['total_all_cost'] or 0
        total_extra = Extra_Charge.objects.aggregate(extra_cost=Sum('extra_charge'))['extra_cost'] or 0
        grand_total = (total_cost + total_extra) / total_meals if total_meals > 0 else 0

        # Combine pagination results + extra info
        response_data = paginated_response.data if page is not None else serializer.data
        response = {
            "results": response_data,
            "total_cost": total_cost,
            "total_extra": total_extra,
            "total_all_meals": total_meals,
            "grand_total": grand_total
        }

        return Response(response)