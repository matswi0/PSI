from rest_framework import serializers, permissions
from .models import DaneKontaktowe, AdresDostawy, Klienci, AdresyZamieszkania, Zarobki, StatusDostawcy, Dostawcy, DanePlatnosci, Zamowienia, Restouracje, Produkty, AdresyRestouracji


class DaneKontaktoweSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaneKontaktowe
        fields = '__all__'


class AdresDostawySerializer(serializers.HyperlinkedModelSerializer):
    klienci = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='klienci-detail')
    class Meta:
        model = AdresDostawy
        fields = '__all__'


class KlienciSerializer(serializers.HyperlinkedModelSerializer):
    adres_dostawy_id  =serializers.SlugRelatedField(queryset=AdresDostawy.objects.all(), slug_field='miejscowosc')
    dane_kontaktowe_id = serializers.SlugRelatedField(queryset=DaneKontaktowe.objects.all(), slug_field='numer_telefonu')
    class Meta:
        model = Klienci
        fields = '__all__'


class AdresyZamieszkaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdresyZamieszkania
        fields = '__all__'


class ZarobkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zarobki
        fields = '__all__'


class StatusDostawcySerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDostawcy
        fields = '__all__'

class DostawcySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dostawcy
        fields = '__all__'


class DanePlatnosciSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanePlatnosci
        fields = '__all__'


class ZamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienia
        fields = '__all__'


class RestouracjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restouracje
        fields = '__all__'

class ProduktySerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkty
        fields = '__all__'


class AdresyRestouracjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdresyRestouracji
        fields = '__all__'