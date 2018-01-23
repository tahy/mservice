from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from provider.models import Area, Provider, Service


class AreaSerializer(GeoFeatureModelSerializer):
    """зоны обслуживания"""

    class Meta:
        model = Area
        geo_field = "polygon"
        fields = ('id', 'name', 'provider', 'service', 'price')


class ProviderSerializer(serializers.ModelSerializer):
    """поставщики услуг"""

    area_set = AreaSerializer(many=True, read_only=True)

    class Meta:
        model = Provider
        fields = ('id', 'name', 'mail', 'phone', 'address', 'area_set')


class ServiceSerializer(serializers.ModelSerializer):
    """услуги"""

    class Meta:
        model = Service
        fields = ('id', 'name',)


class SearchSerializer(serializers.Serializer):
    """Сериалайзер для поиска"""

    provider = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    service = serializers.CharField(max_length=200)