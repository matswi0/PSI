from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from rest_framework import status
from django.utils.http import urlencode
from django import urls




class ZarobkiTests(APITestCase):
    def post_godziny(self, godziny):
        url = reverse(views.AdresyZamieszkaniaList.name)
        data = {'przepracowane_godziny': godziny}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_adres_zamieszkania(self):
        nowe_przepracowane_godziny = 14
        response = self.post_godziny(nowe_przepracowane_godziny)
        assert response.status_code == status.HTTP_201_CREATED
        assert Zarobki.objects.count() == 1
        assert Zarobki.objects.get().godziny == nowe_przepracowane_godziny