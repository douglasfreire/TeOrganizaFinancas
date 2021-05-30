from django.contrib.auth.models import User
from django.db import models
from banco.models import BanksUsers


class Income(models.Model):
    id_bank = models.ForeignKey(BanksUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    release_date_of = models.DateField()
    posted_value = models.BigIntegerField()
    description = models.CharField(max_length=255)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_bank, \
               self.name, \
               self.release_date_of, \
               self.posted_value, \
               self.description, \
               self.id_user
