from rest_framework.viewsets import ModelViewSet
from Billing.models import month,AddMemberMoney
from rest_framework import mixins,viewsets
from Billing.serializers import monthSerializers,AddMemberMoneySerializers
from api.permissions import IsStaffOrReadOnly

class monthViewsSet(ModelViewSet):
    serializer_class=monthSerializers
    queryset = month.objects.all()
    permission_classes = [IsStaffOrReadOnly]




class AddMemberMoneyViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    serializer_class=AddMemberMoneySerializers
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        user=self.request.user
        if user.is_staff:
            return AddMemberMoney.objects.all()

        return AddMemberMoney.objects.filter(member=user)