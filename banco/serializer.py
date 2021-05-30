from rest_framework.serializers import ModelSerializer

from banco.models import ListBanks, BanksUsers


class BankListSerializer(ModelSerializer):
    class Meta:
        model = ListBanks
        fields = ('id', 'name')


class BanksUserSerializer(ModelSerializer):
    class Meta:
        model = BanksUsers
        fields = ('id', 'id_list_banks', 'bank_balance', 'id_user')
