from django.contrib.auth.models import User
from django.db import models


from banco.models import BanksUsers


class Histories(models.Model):
    id_bank = models.ForeignKey(BanksUsers, on_delete=models.CASCADE)
    payment_date = models.DateField()
    due_date = models.DateField()
    name = models.CharField(max_length=30)
    value = models.BigIntegerField()
    description = models.CharField(max_length=255)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fees = models.IntegerField()
    total_bank_balance = models.BigIntegerField()
    balance_available = models.BigIntegerField()

    def __str__(self):
        return self.id_bank, self.payment_date, self.due_date, \
               self.name, self.value, self.description, self.id_user, \
               self.fees, self.total_bank_balance, self.balance_available
