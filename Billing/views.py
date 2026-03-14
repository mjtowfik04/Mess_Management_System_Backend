import pandas as pd
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from Billing.models import month, AddMemberMoney
from Billing.serializers import monthSerializers, AddMemberMoneySerializers
from api.permissions import IsStaffOrReadOnly



class monthViewsSet(viewsets.ModelViewSet):
    serializer_class = monthSerializers
    queryset = month.objects.all()
    permission_classes = [IsStaffOrReadOnly]

class AddMemberMoneyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = AddMemberMoneySerializers
    permission_classes = [IsStaffOrReadOnly]
    

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return AddMemberMoney.objects.all()
        return AddMemberMoney.objects.filter(member=user)

    # 🔹 Custom action: JSON monthly report
    @action(detail=False, methods=['GET'], url_path='monthly-report')
    def monthly_report(self, request):
        user = request.user

        # Queryset fetch
        if user.is_staff:
            qs = AddMemberMoney.objects.all().values(
                "member__email",
                "month__name",
                "deposit_amount"
            )
        else:
            qs = AddMemberMoney.objects.filter(member=user).values(
                "member__email",
                "month__name",
                "deposit_amount"
            )

        df = pd.DataFrame(qs)

        if df.empty:
            return Response({"message": "No data found"}, status=404)

        # Group by month and sum deposit_amount
        report = df.groupby("month__name")["deposit_amount"].sum().reset_index()
        report = report.rename(columns={"month__name": "Month", "deposit_amount": "Total Deposit"})

        return Response(report.to_dict(orient="records"))

    # 🔹 Custom action: CSV download
    @action(detail=False, methods=['GET'], url_path='monthly-report-csv')
    def monthly_report_csv(self, request):
        user = request.user

        if user.is_staff:
            qs = AddMemberMoney.objects.all().values(
                "member__email",
                "month__name",
                "deposit_amount"
            )
        else:
            qs = AddMemberMoney.objects.filter(member=user).values(
                "member__email",
                "month__name",
                "deposit_amount"
            )

        df = pd.DataFrame(qs)

        if df.empty:
            return Response({"message": "No data found"}, status=404)

        report = df.groupby("month__name")["deposit_amount"].sum().reset_index()
        report = report.rename(columns={"month__name": "Month", "deposit_amount": "Total Deposit"})

        # CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="monthly_report.csv"'
        report.to_csv(path_or_buf=response, index=False)
        return response