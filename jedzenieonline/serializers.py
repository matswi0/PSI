from rest_framework import serializers, permissions
from .models import DaneKontaktowe, AdresDostawy, Klienci, AdresyZamieszkania, Zarobki, StatusDostawcy, Dostawcy, DanePlatnosci, Zamowienia, Restauracje, Produkty, AdresyRestauracji


class DaneKontaktoweSerializer(serializers.HyperlinkedModelSerializer):
    klienci = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='klienci-detail')
    dostawcy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='dostawcy-detail')
    class Meta:
        model = DaneKontaktowe
        fields = '__all__'


class AdresDostawySerializer(serializers.HyperlinkedModelSerializer):
    klienci = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='klienci-detail')
    class Meta:
        model = AdresDostawy
        fields = '__all__'


class KlienciSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    adres_dostawy_id  =serializers.SlugRelatedField(queryset=AdresDostawy.objects.all(), slug_field='miejscowosc')
    dane_kontaktowe_id = serializers.SlugRelatedField(queryset=DaneKontaktowe.objects.all(), slug_field='numer_telefonu')
    class Meta:
        model = Klienci
        fields = '__all__'


class AdresyZamieszkaniaSerializer(serializers.HyperlinkedModelSerializer):
    dostawcy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='dostawcy-detail')
    class Meta:
        model = AdresyZamieszkania
        fields = '__all__'


class ZarobkiSerializer(serializers.HyperlinkedModelSerializer):
    dostawcy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='dostawcy-detail')
    class Meta:
        model = Zarobki
        fields = '__all__'


class StatusDostawcySerializer(serializers.HyperlinkedModelSerializer):
    dostawcy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='dostawcy-detail')
    class Meta:
        model = StatusDostawcy
        fields = '__all__'

class DostawcySerializer(serializers.HyperlinkedModelSerializer):
    dane_kontaktowe_id = serializers.SlugRelatedField(queryset=DaneKontaktowe.objects.all(), slug_field='numer_telefonu')
    adresy_zamieszkania_id = serializers.SlugRelatedField(queryset=AdresyZamieszkania.objects.all(), slug_field='miejscowosc')
    status_dostawcy_id = serializers.SlugRelatedField(queryset=StatusDostawcy.objects.all(), slug_field='dostepnosc_dostawcy')
    zarobki_id = serializers.SlugRelatedField(queryset=Zarobki.objects.all(), slug_field='stawka_godzinowa')
    class Meta:
        model = Dostawcy
        fields = '__all__'


class DanePlatnosciSerializer(serializers.HyperlinkedModelSerializer):
    klienci_id = serializers.SlugRelatedField(queryset=Klienci.objects.all(), slug_field='nazwisko')
    class Meta:
        model = DanePlatnosci
        fields = '__all__'


class ZamowieniaSerializer(serializers.HyperlinkedModelSerializer):
    dostawcy_id = serializers.SlugRelatedField(queryset=Dostawcy.objects.all(), slug_field='pesel')
    dane_platnosci_id = serializers.SlugRelatedField(queryset=DanePlatnosci.objects.all(), slug_field='data_platnosci')
    class Meta:
        model = Zamowienia
        fields = '__all__'


class RestauracjeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restauracje
        fields = '__all__'

class ProduktySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produkty
        fields = '__all__'


class AdresyRestauracjiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdresyRestauracji
        fields = '__all__'