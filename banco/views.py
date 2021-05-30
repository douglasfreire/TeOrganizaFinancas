from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from banco.models import ListBanks, BanksUsers
from banco.serializer import BankListSerializer, BanksUserSerializer


def bancotest(request):
    return HttpResponse('banco')


class ListBankViewSet(ModelViewSet):
    queryset = ListBanks.objects.all()
    serializer_class = BankListSerializer


class BanksUsersViewSet(ModelViewSet):
    queryset = BanksUsers.objects.all()
    serializer_class = BanksUserSerializer
