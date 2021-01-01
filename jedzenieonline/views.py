from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, permissions
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import DaneKontaktowe, AdresDostawy, Klienci, AdresyZamieszkania, Zarobki, StatusDostawcy, Dostawcy, DanePlatnosci, Zamowienia, Restouracje, Produkty, AdresyRestouracji
from .serializers import DaneKontaktoweSerializer, AdresDostawySerializer, KlienciSerializer, AdresyZamieszkaniaSerializer, ZarobkiSerializer, StatusDostawcySerializer, DostawcySerializer, DanePlatnosciSerializer, ZamowieniaSerializer, RestouracjeSerializer, ProduktySerializer, AdresyRestouracjiSerializer

# DaneKontaktoweView
class DaneKontaktoweList(APIView):
    def get(self, request):
        dane_kontaktowe = DaneKontaktowe.objects.all()
        serializer = DaneKontaktoweSerializer(dane_kontaktowe, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DaneKontaktowe(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DaneKontaktoweDetail(APIView):
    def get_object(self, pk):
        try:
            return DaneKontaktowe.objects.get(pk=pk)
        except DaneKontaktowe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dane_kontaktowe = self.get_object(pk)
        serializer = DaneKontaktoweSerializer(dane_kontaktowe)
        return Response(serializer.data)

    def put(self, request, pk):
        dane_kontaktowe = self.get_object(pk)
        serializer = DaneKontaktoweSerializer(dane_kontaktowe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dane_kontaktowe = self.get_object(pk)
        dane_kontaktowe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


# AdresDostawyView
class AdresDostawyList(APIView):
    def get(self, request):
        adres_dostawy = AdresDostawy.objects.all()
        serializer = AdresDostawySerializer(adres_dostawy, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdresDostawySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdresDostawyDetail(APIView):
    def get_object(self, pk):
        try:
            return AdresDostawy.objects.get(pk=pk)
        except AdresDostawy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        adres_dostawy = self.get_object(pk)
        serializer = AdresDostawySerializer(adres_dostawy)
        return Response(serializer.data)

    def put(self, request, pk):
        adres_dostawy = self.get_object(pk)
        serializer = AdresDostawySerializer(adres_dostawy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        adres_dostawy = self.get_object(pk)
        adres_dostawy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


# KlienciView
class KlienciList(APIView):
    def get(self, request):
        klienci = Klienci.objects.all()
        serializer = KlienciSerializer(klienci, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KlienciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KlienciDetail(APIView):
    def get_object(self, pk):
        try:
            return Klienci.objects.get(pk=pk)
        except Klienci.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        klienci = self.get_object(pk)
        serializer = KlienciSerializer(klienci)
        return Response(serializer.data)

    def put(self, request, pk):
        klienci = self.get_object(pk)
        serializer = KlienciSerializer(klienci, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        klienci = self.get_object(pk)
        klienci.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

# AdresyZamieszkaniaView
class AdresyZamieszkaniaList(APIView):
    def get(self, request):
        adresy_zamieszkania = AdresyZamieszkania.objects.all()
        serializer = AdresyZamieszkaniaSerializer(adresy_zamieszkania, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdresyZamieszkaniaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdresyZamieszkaniaDetail(APIView):
    def get_object(self, pk):
        try:
            return AdresyZamieszkania.objects.get(pk=pk)
        except AdresyZamieszkania.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        adresy_zamieszkania = self.get_object(pk)
        serializer = AdresyZamieszkaniaSerializer(adresy_zamieszkania)
        return Response(serializer.data)

    def put(self, request, pk):
        adresy_zamieszkania = self.get_object(pk)
        serializer = AdresyZamieszkaniaSerializer(adresy_zamieszkania, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        adresy_zamieszkania = self.get_object(pk)
        adresy_zamieszkania.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


# ZarobkiView
class ZarobkiList(APIView):
    def get(self, request):
        zarobki = Zarobki.objects.all()
        serializer = ZarobkiSerializer(zarobki, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ZarobkiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ZarobkiDetail(APIView):
    def get_object(self, pk):
        try:
            return Zarobki.objects.get(pk=pk)
        except Zarobki.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        zarobki = self.get_object(pk)
        serializer = ZarobkiSerializer(zarobki)
        return Response(serializer.data)

    def put(self, request, pk):
        zarobki = self.get_object(pk)
        serializer = ZarobkiSerializer(zarobki, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        zarobki = self.get_object(pk)
        zarobki.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

# StatusDostawcyView
class StatusDostawcyList(APIView):
    def get(self, request):
        status_dostawcy = StatusDostawcy.objects.all()
        serializer = StatusDostawcySerializer(status_dostawcy, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StatusDostawcySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusDostawcyDetail(APIView):
    def get_object(self, pk):
        try:
            return StatusDostawcy.objects.get(pk=pk)
        except StatusDostawcy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        status_dostawcy = self.get_object(pk)
        serializer = StatusDostawcySerializer(status_dostawcy)
        return Response(serializer.data)

    def put(self, request, pk):
        status_dostawcy = self.get_object(pk)
        serializer = StatusDostawcySerializer(status_dostawcy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        status_dostawcy = self.get_object(pk)
        status_dostawcy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


# DostawcyView
class DostawcyList(APIView):
    def get(self, request):
        dostawcy = Dostawcy.objects.all()
        serializer = DostawcySerializer(dostawcy, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DostawcySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DostawcyDetail(APIView):
    def get_object(self, pk):
        try:
            return Dostawcy.objects.get(pk=pk)
        except Dostawcy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dostawcy = self.get_object(pk)
        serializer = DostawcySerializer(dostawcy)
        return Response(serializer.data)

    def put(self, request, pk):
        dostawcy = self.get_object(pk)
        serializer = DostawcySerializer(dostawcy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dostawcy = self.get_object(pk)
        dostawcy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


# DanePlatnosciView
class DanePlatnosciList(APIView):
    def get(self, request):
        dane_platnosci = DanePlatnosci.objects.all()
        serializer = DanePlatnosciSerializer(dane_platnosci, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DanePlatnosciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DanePlatnosciDetail(APIView):
    def get_object(self, pk):
        try:
            return DanePlatnosci.objects.get(pk=pk)
        except DanePlatnosci.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dane_platnosci = self.get_object(pk)
        serializer = DanePlatnosciSerializer(dane_platnosci)
        return Response(serializer.data)

    def put(self, request, pk):
        dane_platnosci = self.get_object(pk)
        serializer = DanePlatnosciSerializer(dane_platnosci, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dane_platnosci = self.get_object(pk)
        dane_platnosci.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


# ZamowieniaView
class ZamowieniaList(APIView):
    def get(self, request):
        zamowienia = Zamowienia.objects.all()
        serializer = ZamowieniaSerializer(zamowienia, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ZamowieniaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ZamowieniaDetail(APIView):
    def get_object(self, pk):
        try:
            return Zamowienia.objects.get(pk=pk)
        except Zamowienia.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        zamowienia = self.get_object(pk)
        serializer = ZamowieniaSerializer(zamowienia)
        return Response(serializer.data)

    def put(self, request, pk):
        zamowienia = self.get_object(pk)
        serializer = ZamowieniaSerializer(zamowienia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        zamowienia = self.get_object(pk)
        zamowienia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


# RestouracjeView
class RestouracjeList(APIView):
    def get(self, request):
        restouracje = Restouracje.objects.all()
        serializer = RestouracjeSerializer(restouracje, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestouracjeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestouracjeDetail(APIView):
    def get_object(self, pk):
        try:
            return Restouracje.objects.get(pk=pk)
        except Restouracje.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        restouracje = self.get_object(pk)
        serializer = RestouracjeSerializer(restouracje)
        return Response(serializer.data)

    def put(self, request, pk):
        restouracje = self.get_object(pk)
        serializer = RestouracjeSerializer(restouracje, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restouracje = self.get_object(pk)
        restouracje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


# ProduktyView
class ProduktyList(APIView):
    def get(self, request):
        produkty = Produkty.objects.all()
        serializer = ProduktySerializer(produkty, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProduktySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProduktyDetail(APIView):
    def get_object(self, pk):
        try:
            return Produkty.objects.get(pk=pk)
        except Produkty.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        produkty = self.get_object(pk)
        serializer = ProduktySerializer(produkty)
        return Response(serializer.data)

    def put(self, request, pk):
        produkty = self.get_object(pk)
        serializer = ProduktySerializer(produkty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        produkty = self.get_object(pk)
        produkty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]



# AdresyRestouracjiView
class AdresyRestouracjiList(APIView):
    def get(self, request):
        adresy_restouracji = AdresyRestouracji.objects.all()
        serializer = AdresyRestouracjiSerializer(adresy_restouracji, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdresyRestouracjiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdresyRestouracjiDetail(APIView):
    def get_object(self, pk):
        try:
            return AdresyRestouracji.objects.get(pk=pk)
        except AdresyRestouracji.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        adresy_restouracji = self.get_object(pk)
        serializer = AdresyRestouracjiSerializer(adresy_restouracji)
        return Response(serializer.data)

    def put(self, request, pk):
        adresy_restouracji = self.get_object(pk)
        serializer = AdresyRestouracjiSerializer(adresy_restouracji, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        adresy_restouracji = self.get_object(pk)
        adresy_restouracji.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]