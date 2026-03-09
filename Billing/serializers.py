from Billing.models import month,AddMemberMoney
from rest_framework import serializers
class monthSerializers(serializers.ModelSerializer):
    class Meta:
        model=month
        fields = '__all__'

        
class AddMemberMoneySerializers(serializers.ModelSerializer):
    class Meta:
        model=AddMemberMoney
        fields='__all__'