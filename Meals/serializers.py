from rest_framework import serializers
from Meals.models import meal

class MealSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    # member_name = serializers.CharField(source="member.username", read_only=True)
    member_email = serializers.EmailField(source="member.email", read_only=True)

    class Meta:
        model = meal
        fields = [
            "id",
            "date",
            "lunch",
            "dinner",
            "is_guest",
            "freeze",
            "member",
            # "member_name",   # username
            "member_email",  # email
            "month",
            "total",
        ]

    def get_total(self, obj):
        return obj.total_meal()