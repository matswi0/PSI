from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from rest_framework import status
from .models import AdresDostawy, DaneKontaktowe
from django.utils.http import urlencode
from django import urls




class AdresDostawyTests(APITestCase):
    def post_adres_dostawy(self, miejscowosc):
        url = reverse(views.AdresDostawyList.name)
        data = {'miejscowosc': miejscowosc}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_adres_dostawy(self):
        nowa_miejscowosc = 'Warszawa'
        response = self.post_adres_dostawy(nowa_miejscowosc)
        assert response.status_code == status.HTTP_201_CREATED
        assert AdresDostawy.objects.count() == 1
        assert AdresDostawy.objects.get().miejscowosc == nowa_miejscowosc


    def test_post_existing_adres_dostawy(self):
        url = reverse(views.AdresDostawyList.name)
        nowa_miejscowosc = 'Duplicate Warszawa'
        data = {'miejscowosc': nowa_miejscowosc}
        response_one = self.post_adres_dostawy(nowa_miejscowosc)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_adres_dostawy(nowa_miejscowosc)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_book_category_by_name(self):
        miejscowosc_name_one = 'Olsztyn'
        miejscowosc_name_two = 'Warszawa'
        self.post_adres_dostawy(miejscowosc_name_one)
        self.post_adres_dostawy(miejscowosc_name_two)
        filter_by_name = {'miejscowosc': miejscowosc_name_one}
        url = '{0}?{1}'.format(reverse(views.AdresDostawyList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['miejscowosc'] == miejscowosc_name_one

    def test_get_adres_dostawy_collection(self):
        new_miejscowosc = 'Super Copter'
        self.post_adres_dostawy(new_miejscowosc)
        url = reverse(views.AdresDostawyList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['miejscowosc'] == new_miejscowosc

    def test_update_adres_dostawy(self):
        miejscowosc = 'Suwalki'
        response = self.post_adres_dostawy(miejscowosc)
        url = urls.reverse(views.AdresDostawyDetail.name, None, {response.data['pk']})
        updated_miejscowosc = 'New IT'
        data = {'miejscowosc': updated_miejscowosc}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['miejscowosc'] == updated_miejscowosc

    def test_get_adres_dostawy(self):
        miejscowosc = 'Olsztyn'
        response = self.post_adres_dostawy(miejscowosc)
        url = urls.reverse(views.AdresDostawyDetail.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['miejscowosc'] == miejscowosc



class DaneKontaktoweTests(APITestCase):
    def post_dane_kontaktowe(self, numer_telefonu):
        url = reverse(views.DaneKontaktoweList.name)
        data = {'numer_telefonu': numer_telefonu}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_dane_kontaktowe(self):
        nowy_numer_telefonu = '666555444'
        response = self.post_dane_kontaktowe(nowy_numer_telefonu)
        assert response.status_code == status.HTTP_201_CREATED
        assert DaneKontaktowe.objects.count() == 1
        assert DaneKontaktowe.objects.get().numer_telefonu == nowy_numer_telefonu


    def test_post_existing_dane_kontaktowe(self):
        url = reverse(views.DaneKontaktoweList.name)
        nowy_numer_telefonu= 'Duplicate 666555444'
        data = {'numer_telefonu': nowy_numer_telefonu}
        response_one = self.post_dane_kontaktowe(nowy_numer_telefonu)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_dane_kontaktowe(nowy_numer_telefonu)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_dane_kontaktowe_by_name(self):
        numer_telefonu_one = '123456789'
        numer_telefonu_two = '987654321'
        self.post_dane_kontaktowe(numer_telefonu_one)
        self.post_dane_kontaktowe(numer_telefonu_two)
        filter_by_name = {'numer_telefonu': numer_telefonu_one}
        url = '{0}?{1}'.format(reverse(views.DaneKontaktoweList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['numer_telefonu'] == numer_telefonu_one

    def test_get_dane_kontaktowe_collection(self):
        new_numer = '444444444'
        self.post_dane_kontaktowe(new_numer)
        url = reverse(views.DaneKontaktoweList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['numer_telefonu'] == new_numer

    def test_update_dane_kontaktowe(self):
        numer_telefonu = '777777777'
        response = self.post_dane_kontaktowe(numer_telefonu)
        url = urls.reverse(views.DaneKontaktoweDetail.name, None, {response.data['pk']})
        updated_numer = '666666666'
        data = {'numer_telefonu': updated_numer}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['numer_telefonu'] == updated_numer

    def test_get_adres_dostawy(self):
        numer_telefonu = '333333333'
        response = self.post_dane_kontaktowe(numer_telefonu)
        url = urls.reverse(views.DaneKontaktoweDetail.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['numer_telefonu'] == numer_telefonu




