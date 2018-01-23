from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from provider.models import Area, Provider, Service
from provider.serializers import AreaSerializer, ProviderSerializer, ServiceSerializer, SearchSerializer


class AreaList(viewsets.ModelViewSet):
    """CRUD для зон обслуживания"""

    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class ProviderList(viewsets.ModelViewSet):
    """CRUD для поставщиков услуг"""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceList(viewsets.ModelViewSet):
    """CRUD для услуг"""

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SearchView(APIView):
    """Поиск"""

    def get(self, request, format=None):
        queryset = Area.objects.all()

        point_string = request.query_params.get('point', None)
        if point_string:
            try:
                (x, y) = (float(n) for n in point_string.split(','))
            except ValueError:
                raise ParseError('Invalid geometry string supplied for parameter {0}'.format(self.point_param))

            p = Point(x, y)
            queryset = queryset.filter(Q(**{'polygon__dwithin': (p, 0)}))

        service_string = request.query_params.get('service', None)
        if point_string:
            queryset = queryset.filter(service_id=service_string)

        serializer = SearchSerializer(queryset, many=True)
        return Response(serializer.data)