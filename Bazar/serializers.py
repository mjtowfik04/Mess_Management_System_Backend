from rest_framework import serializers
from .models import Add_Cost,Extra_Charge

class Add_Cost_serializers(serializers.ModelSerializer):
    # total_cost=serializers.SerializerMethodField()
    class Meta:
        model=Add_Cost
        fields=['month','meal_cost','meal_Bazar_details','member','date_time']

    # def get_total_cost(self,):

class Extra_Charge_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Extra_Charge
        fields=['month','extra_charge','date_time']




