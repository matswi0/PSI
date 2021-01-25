from rest_framework import serializers, permissions
from .models import DaneKontaktowe, AdresDostawy, Klienci, AdresyZamieszkania, Dostawcy, DanePlatnosci, Zamowienia, Restauracje, Produkty, AdresyRestauracji
from django.contrib.auth.models import User

class UserKlientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Klienci
        fields = ['url', 'imie', 'nazwisko']

class UserProduktSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produkty
        fields = ['url', 'nazwa_produktu']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    klienci = UserKlientSerializer(many=True, read_only=True)
    produkty = UserProduktSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'klienci', 'produkty')



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
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')
    class Meta:
        model = Klienci
        fields = '__all__'


class AdresyZamieszkaniaSerializer(serializers.HyperlinkedModelSerializer):
    dostawcy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='dostawcy-detail')
    class Meta:
        model = AdresyZamieszkania
        fields = '__all__'


class DostawcySerializer(serializers.HyperlinkedModelSerializer):
    dane_kontaktowe_id = serializers.SlugRelatedField(queryset=DaneKontaktowe.objects.all(), slug_field='numer_telefonu')
    adresy_zamieszkania_id = serializers.SlugRelatedField(queryset=AdresyZamieszkania.objects.all(), slug_field='miejscowosc')
    class Meta:
        model = Dostawcy
        fields = '__all__'


class DanePlatnosciSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DanePlatnosci
        fields = '__all__'


class ZamowieniaSerializer(serializers.HyperlinkedModelSerializer):
    dostawcy_id = serializers.SlugRelatedField(queryset=Dostawcy.objects.all(), slug_field='pesel')

    class Meta:
        model = Zamowienia
        fields = '__all__'


class RestauracjeSerializer(serializers.HyperlinkedModelSerializer):
    adresy_restauracji = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='adresyrestauracji-detail')
    produkty = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='produkty-detail')
    class Meta:
        model = Restauracje
        fields = '__all__'

class ProduktySerializer(serializers.HyperlinkedModelSerializer):
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')
    restauracja_id = serializers.SlugRelatedField(queryset=Restauracje.objects.all(), slug_field='nazwa_restauracji')
    class Meta:
        model = Produkty
        fields = '__all__'


class AdresyRestauracjiSerializer(serializers.HyperlinkedModelSerializer):
    restauracja_id = serializers.SlugRelatedField(queryset=Restauracje.objects.all(), slug_field='nazwa_restauracji')
    class Meta:
        model = AdresyRestauracji
        fields = '__all__'