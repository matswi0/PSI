from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import status, permissions
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import DaneKontaktowe, AdresDostawy, Klienci, AdresyZamieszkania, Dostawcy, DanePlatnosci, Zamowienia, Restauracje, Produkty, AdresyRestauracji
from .serializers import DaneKontaktoweSerializer, AdresDostawySerializer, KlienciSerializer, AdresyZamieszkaniaSerializer, DostawcySerializer, DanePlatnosciSerializer, ZamowieniaSerializer, RestauracjeSerializer, ProduktySerializer, AdresyRestauracjiSerializer, UserSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from django.contrib.auth.models import User

# UserView
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

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
    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.user)


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


# RestauracjeView
class RestauracjeList(generics.ListCreateAPIView):
    queryset = Restauracje.objects.all()
    serializer_class = RestauracjeSerializer
    name = 'restauracje-list'
    filterset_fields = ['nazwa_restauracji']
    search_fields = ['nazwa_restauracji']
    ordering_fields = ['nazwa_restauracji']


class RestauracjeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restauracje.objects.all()
    serializer_class = RestauracjeSerializer
    name = 'restauracje-detail'


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
    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.user)

class ProduktyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer
    name = 'produkty-detail'


# AdresyRestauracjiView
class AdresyRestauracjiFilter(FilterSet):
    nazwa_miej = AllValuesFilter(field_name='miejscowosc')

    class Meta:
        model = AdresyRestauracji
        fields = ['nazwa_miej']

class AdresyRestauracjiList(generics.ListCreateAPIView):
    queryset = AdresyRestauracji.objects.all()
    serializer_class = AdresyRestauracjiSerializer
    name = 'adresyrestauracji-list'
    filter_class = AdresyRestauracjiFilter


class AdresyRestauracjiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdresyRestauracji.objects.all()
    serializer_class = AdresyRestauracjiSerializer
    name = 'adresyrestauracji-detail'
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
                         'dostawcy-list': reverse(DostawcyList.name, request=request),
                         'daneplatnosci-list': reverse(DanePlatnosciList.name, request=request),
                         'zamowienia-list': reverse(ZamowieniaList.name, request=request),
                         'restauracje-list': reverse(RestauracjeList.name, request=request),
                         'produkty-list': reverse(ProduktyList.name, request=request),
                         'adresyrestauracji-list': reverse(AdresyRestauracjiList.name, request=request),
                         'user-list': reverse(UserList.name, request=request)

})

