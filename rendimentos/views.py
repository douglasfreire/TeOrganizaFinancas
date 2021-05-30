from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from rendimentos.models import Income
from rendimentos.serializer import IncomeSerializer


def rend_views_test(request):
    return HttpResponse('rendimentos')


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
