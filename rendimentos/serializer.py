from rest_framework.serializers import ModelSerializer

from rendimentos.models import Income


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ('id_bank', 'name', 'release_date_of', 'posted_value', 'description', 'id_user')
