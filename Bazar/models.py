from django.db import models
from Billing.models import month
from Users.models import User 
from datetime import date

class Add_Cost(models.Model):
    month=models.ForeignKey(month,on_delete=models.CASCADE)
    date_time=models.DateField(default=date.today)
    meal_cost=models.IntegerField()
    meal_Bazar_details=models.CharField(max_length=500,blank=True,null=None)
    member=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.member


class Extra_Charge(models.Model):
    month=models.ForeignKey(month,on_delete=models.CASCADE)
    date_time=models.DateField(default=date.today)

    extra_charge=models.IntegerField()

    def __str__(self):
        return self.extra_charge



    