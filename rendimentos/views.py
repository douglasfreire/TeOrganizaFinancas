from django.http import HttpResponse
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rendimentos.models import Income
from rendimentos.serializer import IncomeSerializer


def rend_views_test(request):
    return HttpResponse('rendimentos')


@api_view(['POST'])
def income(request):
    serializer = IncomeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_income(request):
    income_list = Income.objects.all()
    serializer = IncomeSerializer(income_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def retrieve_income(request, pk):
    try:
        income_object = Income.objects.get(pk=pk)
    except Income.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = IncomeSerializer(income_object)
    return Response(serializer.data)


@api_view(['PUT'])
def update_income(request, pk):
    try:
        income_object = Income.objects.get(pk=pk)
    except income_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = IncomeSerializer(income_object, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def partial_income(request, pk):
    try:
        income_object = Income.objects.get(pk=pk)
    except income_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    income_object.name = request.data.get('name', income_object.name)
    income_object.posted_value = request.data.get('posted_value', income_object.posted_value)
    income_object.description = request.data.get('description', income_object.description)

    income_object.save()
    serializer = IncomeSerializer(income_object)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_income(request, pk):
    income_object = Income.objects.get(pk=pk)
    income_object.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
