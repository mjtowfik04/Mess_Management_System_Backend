from rest_framework.viewsets import ModelViewSet
from Billing.models import month,AddMemberMoney
from rest_framework import mixins,viewsets
from Billing.serializers import monthSerializers,AddMemberMoneySerializers

class monthViewsSet(ModelViewSet):
    serializer_class=monthSerializers
    queryset = month.objects.all()




class AddMemberMoneyViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    serializer_class=AddMemberMoneySerializers
    queryset=AddMemberMoney.objects.all()