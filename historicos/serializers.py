from rest_framework import serializers

from historicos.models import Histories


class HistoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Histories
        fields = '__all__'
        # fields = ["id",
        #           "id_bank",
        #           "payment_date",
        #           "due_date",
        #           "name",
        #           "value",
        #           "description",
        #           "id_user",
        #           "fees",
        #           "total_bank_balance",
        #           "balance_available"
        #           ]
