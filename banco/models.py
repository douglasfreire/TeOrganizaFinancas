from django.contrib.auth.models import User
from django.db import models


class ListBanks(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BanksUsers(models.Model):
    id_list_banks = models.ForeignKey(ListBanks, on_delete=models.PROTECT)
    bank_balance = models.BigIntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_list_banks, self.bank_balance, self.id_user
