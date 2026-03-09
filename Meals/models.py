from django.db import models
from Users.models import  User
from Billing.models  import  month

class meal(models.Model):
    member=models.ForeignKey(User,on_delete=models.CASCADE,related_name='meals')
    month=models.ForeignKey(month,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    lunch=models.IntegerField(default=0)
    dinner=models.IntegerField(default=0)
    is_guest=models.BooleanField(default=False) 
    freeze = models.BooleanField(default=False)  

    def total_meal(self):
        if self.freeze:
            return 0
        total = self.lunch + self.dinner
        if self.is_guest:
            total += 2
        return total
    def __str__(self):
        return self.member.email