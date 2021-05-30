from django.contrib.auth.models import User
from django.db import models


class PaymentsStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Expenses(models.Model):
    due_date = models.DateField()
    name = models.CharField(max_length=30)
    value = models.BigIntegerField()
    description = models.CharField(max_length=255)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fees = models.IntegerField()
    id_payments_status = models.ForeignKey(PaymentsStatus, on_delete=models.PROTECT)

    def __str__(self):
        return self.due_date, \
               self.name, \
               self.value, \
               self.description, \
               self.id_user, \
               self.fees, \
               self.id_payments_status
