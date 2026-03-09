from django.db import models
from Users.models import  User
from django.utils import timezone


class month(models.Model):
    name=models.CharField(max_length=20) 
    start_date=models.DateField()
    end_date=models.DateField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class AddMemberMoney(models.Model):
    month=models.ForeignKey(month,on_delete=models.CASCADE)
    date_time=models.DateField(default=timezone.now,blank=False,null=False)
    deposit_amount=models.IntegerField()
    deposit_details=models.CharField(max_length=500,null=None,blank=True)
    member=models.ForeignKey(User,on_delete=models.CASCADE,related_name='deposits')

    def __str__(self):
        return f"{self.member.email} - {self.deposit_amount}"
    

