from .models import Add_Cost, Extra_Charge
from .serializers import Add_Cost_serializers, Extra_Charge_Serializers
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django.db.models import Sum
from api.permissions import IsStaffOrReadOnly
from api.paginations import DefaultPagination

class AddCostViewSet(
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):

    serializer_class = Add_Cost_serializers
    queryset = Add_Cost.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    pagination_class=DefaultPagination
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # Meal total
        total_cost = queryset.aggregate(total_all_cost=Sum('meal_cost'))['total_all_cost'] or 0

        # Extra charges total (use 'extra_charge' field)
        extra_total = Extra_Charge.objects.aggregate(total_extra=Sum('extra_charge'))['total_extra'] or 0

        # Grand total
        grand_total = total_cost + extra_total

        response = {
            "results": data,
            "total_meals": total_cost,
            "extra_total": extra_total,
            "grand_total_cost": grand_total
        }

        return Response(response)




class ExtraChargeViweSet(
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):

    serializer_class = Extra_Charge_Serializers
    queryset = Extra_Charge.objects.all()
    pagination_class=DefaultPagination


    permission_classes = [IsStaffOrReadOnly]
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        total_ex = Extra_Charge.objects.aggregate(total_all_ex=Sum('extra_charge'))['total_all_ex'] or 0

        response = {
            'results': data,
            'total_ex': total_ex
        }

        return Response(response)