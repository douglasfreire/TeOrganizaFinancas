from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from historicos.models import Histories
from historicos.serializers import HistoriesSerializer


class HistoriesAPIView(APIView):

    def get_queryset(self):
        histories = Histories.objects.all()
        return histories

    def post(self, request):
        serializer = HistoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        histories = self.get_queryset()
        serializer = HistoriesSerializer(histories, many=True)
        return Response(serializer.data)


class HistoriesDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Histories.objects.get(pk=pk)
        except Histories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            histories = self.get_object(pk=pk)
            serializer = HistoriesSerializer(histories)
            return Response(serializer.data)
        except AttributeError:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            histories = self.get_object(pk=pk)
            serializer = HistoriesSerializer(histories, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            histories = self.get_object(pk=pk)
            serializer = HistoriesSerializer(histories, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            histories = self.get_object(pk=pk)
            histories.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_404_NOT_FOUND)
