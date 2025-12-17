from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Company
from app.serializers import CompanySerializer
from rest_framework.pagination import PageNumberPagination




class CompanyListCreateAPIView(APIView):
    def get(self, request):
        LCO = Company.objects.all()
        pagination=PageNumberPagination()
        pagination.page_size=1
        paginateddata=pagination.paginate_queryset(LCO,request)
        SCO = CompanySerializer(paginateddata, many=True)
        return Response(SCO.data)
    def post(self, request):
        Sdata = CompanySerializer(data=request.data)
        if Sdata.is_valid():
            Sdata.save()
            return Response(Sdata.data, status=status.HTTP_201_CREATED)
        return Response(Sdata.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            CO = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        SCO = CompanySerializer(CO)
        return Response(SCO.data)

    def put(self, request, pk):
        try:
            CO = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        SCO = CompanySerializer(CO, data=request.data)
        if SCO.is_valid():
            SCO.save()
            return Response(SCO.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            CO = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        CO.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)