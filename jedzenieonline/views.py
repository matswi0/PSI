from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import status, permissions
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import DaneKontaktowe, AdresDostawy, Klienci, AdresyZamieszkania, Zarobki, StatusDostawcy, Dostawcy, DanePlatnosci, Zamowienia, Restouracje, Produkty, AdresyRestouracji
from .serializers import DaneKontaktoweSerializer, AdresDostawySerializer, KlienciSerializer, AdresyZamieszkaniaSerializer, ZarobkiSerializer, StatusDostawcySerializer, DostawcySerializer, DanePlatnosciSerializer, ZamowieniaSerializer, RestouracjeSerializer, ProduktySerializer, AdresyRestouracjiSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet




# DaneKontaktoweView
class DaneKontaktoweList(generics.ListCreateAPIView):
    queryset = DaneKontaktowe.objects.all()
    serializer_class = DaneKontaktoweSerializer
    name = 'danekontaktowe-list'
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'POST', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

class DaneKontaktoweDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DaneKontaktowe.objects.all()
    serializer_class = DaneKontaktoweSerializer
    name = 'danekontaktowe-detail'

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]



# AdresDostawyView
class AdresDostawyList(generics.ListCreateAPIView):
    queryset = AdresDostawy.objects.all()
    serializer_class = AdresDostawySerializer
    name = 'adresdostawy-list'
    filterset_fields = ['miejscowosc', 'ulica']
    search_fields = ['miejscowosc', 'ulica']
    ordering_fields = ['miejscowosc', 'ulica']

class AdresDostawyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdresDostawy.objects.all()
    serializer_class = AdresDostawySerializer
    name = 'adresdostawy-detail'


# KlienciView

class KlienciList(generics.ListCreateAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-list'
    filterset_fields = ['nazwisko', 'imie']
    search_fields = ['nazwisko', 'imie']
    ordering_fields = ['nazwisko', 'imie']



class KlienciDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-detail'

# AdresyZamieszkaniaView
class AdresyZamieszkaniaList(generics.ListCreateAPIView):
    queryset = AdresyZamieszkania.objects.all()
    serializer_class = AdresyZamieszkaniaSerializer
    name = 'adresyzamieszkania-list'
    filterset_fields = ['miejscowosc', 'ulica']
    search_fields = ['miejscowosc', 'ulica']
    ordering_fields = ['miejscowosc', 'ulica']


class AdresyZamieszkaniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdresyZamieszkania.objects.all()
    serializer_class = AdresyZamieszkaniaSerializer
    name = 'adresyzamieszkania-detail'


# ZarobkiView
class ZarobkiFilter(FilterSet):
    od_okres = DateTimeFilter(field_name='okres_od', lookup_expr='gte')
    do_okres = DateTimeFilter(field_name='okres_do', lookup_expr='lte')

    class Meta:
        model = Zarobki
        fields = ['od_okres', 'do_okres']

class ZarobkiList(generics.ListCreateAPIView):
    queryset = Zarobki.objects.all()
    serializer_class = ZarobkiSerializer
    name = 'zarobki-list'
    filter_class = ZarobkiFilter
    ordering_fields = ['przepracowane_godziny']

class ZarobkiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zarobki.objects.all()
    serializer_class = ZarobkiSerializer
    name = 'zarobki-detail'


# StatusDostawcyView

class StatusDostawcyFilter(FilterSet):
    dostepnosc = AllValuesFilter(field_name='dostepnosc_dostawcy')
    class Meta:
        model = StatusDostawcy
        fields = ['dostepnosc_dostawcy']

class StatusDostawcyList(generics.ListCreateAPIView):
    queryset = StatusDostawcy.objects.all()
    serializer_class = StatusDostawcySerializer
    name = 'statusdostawcy-list'
    filter_class = StatusDostawcyFilter
    ordering_fields = ['data_zatrudnienia', 'data_zwolnienia']


class StatusDostawcyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StatusDostawcy.objects.all()
    serializer_class = StatusDostawcySerializer
    name = 'statusdostawcy-detail'


# DostawcyView
class DostawcyList(generics.ListCreateAPIView):
    queryset = Dostawcy.objects.all()
    serializer_class = DostawcySerializer
    name = 'dostawcy-list'


class DostawcyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dostawcy.objects.all()
    serializer_class = DostawcySerializer
    name = 'dostawcy-detail'


# DanePlatnosciView
class DanePlatnosciFilter(FilterSet):
    od_data = DateTimeFilter(field_name='data_platnosci', lookup_expr='gte')
    do_data = DateTimeFilter(field_name='data_platnosci', lookup_expr='lte')

    class Meta:
        model = DanePlatnosci
        fields = ['od_data', 'do_data']

class DanePlatnosciList(generics.ListCreateAPIView):
    queryset = DanePlatnosci.objects.all()
    serializer_class = DanePlatnosciSerializer
    name = 'daneplatnosci-list'
    filter_class = DanePlatnosciFilter



class DanePlatnosciDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DanePlatnosci.objects.all()
    serializer_class = DanePlatnosciSerializer
    name = 'daneplantosci-detail'


# ZamowieniaView
class ZamowieniaList(generics.ListCreateAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    name = 'zamowienia-list'


class ZamowieniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    name = 'zamowienia-detail'


# RestouracjeView
class RestouracjeList(generics.ListCreateAPIView):
    queryset = Restouracje.objects.all()
    serializer_class = RestouracjeSerializer
    name = 'restouracje-list'
    filterset_fields = ['nazwa_restouracji']
    search_fields = ['nazwa_restouracji']
    ordering_fields = ['nazwa_restouracji']


class RestouracjeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restouracje.objects.all()
    serializer_class = RestouracjeSerializer
    name = 'restouracje-detail'


# ProduktyView
class ProduktyFilter(FilterSet):
    od_cena = NumberFilter(field_name='cena', lookup_expr='gte')
    do_cena = NumberFilter(field_name='cena', lookup_expr='lte')

    class Meta:
        model = Produkty
        fields = ['od_cena', 'do_cena']


class ProduktyList(generics.ListCreateAPIView):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer
    name = 'produkty-list'
    filter_class = ProduktyFilter


class ProduktyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer
    name = 'produkty-detail'


# AdresyRestouracjiView
class AdresyRestouracjiFilter(FilterSet):
    nazwa_miej = AllValuesFilter(field_name='miejscowosc')

    class Meta:
        model = AdresyRestouracji
        fields = ['nazwa_miej']

class AdresyRestouracjiList(generics.ListCreateAPIView):
    queryset = AdresyRestouracji.objects.all()
    serializer_class = AdresyRestouracjiSerializer
    name = 'adresyrestouracji-list'
    filter_class = AdresyRestouracjiFilter


class AdresyRestouracjiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdresyRestouracji.objects.all()
    serializer_class = AdresyRestouracjiSerializer
    name = 'adresyrestouracji-detail'
    filterset_fields = ['miejscowosc', 'ulica']
    search_fields = ['miejscowosc', 'ulica']
    ordering_fields = ['miejscowosc', 'ulica']


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'danekontaktowe-list': reverse(DaneKontaktoweList.name, request=request),
                         'adresdostawy-list': reverse(AdresDostawyList.name, request=request),
                         'klienci-list': reverse(KlienciList.name, request=request),
                         'adresyzamieszkania-list': reverse(AdresyZamieszkaniaList.name, request=request),
                         'zarobki-list': reverse(ZarobkiList.name, request=request),
                         'statusdostawcy-list': reverse(StatusDostawcyList.name, request=request),
                         'dostawcy-list': reverse(DostawcyList.name, request=request),
                         'daneplatnosci-list': reverse(DanePlatnosciList.name, request=request),
                         'zamowienia-list': reverse(ZamowieniaList.name, request=request),
                         'restouracje-list': reverse(RestouracjeList.name, request=request),
                         'produkty-list': reverse(ProduktyList.name, request=request),
                         'adresyrestouracji-list': reverse(AdresyRestouracjiList.name, request=request)

})

