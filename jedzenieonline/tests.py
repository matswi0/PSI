from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from rest_framework import status
from .models import AdresDostawy
from django.utils.http import urlencode
from django import urls




class AdresDostawyTests(APITestCase):
    def post_godziny(self, miejscowosc):
        url = reverse(views.AdresDostawyList.name)
        data = {'miejscowosc': miejscowosc}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_adres_zamieszkania(self):
        nowa_miejscowosc = 'Warszawa'
        response = self.post_godziny(nowa_miejscowosc)
        assert response.status_code == status.HTTP_201_CREATED
        assert AdresDostawy.objects.count() == 1
        assert AdresDostawy.objects.get().miejscowosc == nowa_miejscowosc