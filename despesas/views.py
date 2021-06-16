from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from despesas.models import Expenses
from despesas.serializers import ExpensesSerializer


def despesastest(request):
    return Response('despesas')


class ExpensesAPIView(APIView):
    serializer_class = ExpensesSerializer

    def get_queryset(self):
        expenses = Expenses.objects.all()
        return expenses

    def get(self, request):
        expenses = self.get_queryset()
        serializer = ExpensesSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetailApiView(APIView):

    def get_object(self, pk):
        try:
            return Expenses.objects.get(pk=pk)
        except Expenses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        expense = self.get_object(pk=pk)
        serializer = ExpensesSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            expense = self.get_object(pk=pk)
        except Expenses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExpensesSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            expense = self.get_object(pk=pk)
        except Expenses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            expense = self.get_object(pk=pk)
        except Expenses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExpensesSerializer(expense, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
