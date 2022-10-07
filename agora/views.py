from rest_framework import status
from rest_framework import viewsets
from .models import Companies, Advocates
from .serializers import CompaniesSerializer, AdvocatesSerializer, RetrieveAdvocatesSerializer, \
    CompanyAdvocatesSerializer
from rest_framework.response import Response


# Create your views here.

class AdvocatesViewSets(viewsets.ModelViewSet):
    queryset = Advocates.objects.all()
    serializer_class = AdvocatesSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.queryset
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = RetrieveAdvocatesSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CompaniesViewSets(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        advocates = Advocates.objects.filter(company=instance)
        serializer = self.serializer_class(instance)
        advocates_serializer = CompanyAdvocatesSerializer(advocates, many=True)
        data = serializer.data
        data["advocates"] = advocates_serializer.data
        return Response({'company': data},
                        status=status.HTTP_200_OK)
