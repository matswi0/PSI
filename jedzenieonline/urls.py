from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    # DaneKontaktoweURL
    path('danekontaktowe-list', views.DaneKontaktoweList.as_view(), name=views.DaneKontaktoweList.name),
    path('danekontaktowe-detail/<int:pk>', views.DaneKontaktoweDetail.as_view(), name=views.DaneKontaktoweDetail.name),

    # AdresDostawyURL
    path('adresdostawy-list', views.AdresDostawyList.as_view(), name=views.AdresDostawyList.name),
    path('adresdostawy-detail/<int:pk>', views.AdresDostawyDetail.as_view(), name=views.AdresDostawyDetail.name),

    # KlienciURL
    path('klienci-list', views.KlienciList.as_view(), name=views.KlienciList.name),
    path('klienci-detail/<int:pk>', views.KlienciDetail.as_view(), name=views.KlienciDetail.name),

    # AdresyZamieszkaniaURL
    path('adresyzamieszkania-list', views.AdresyZamieszkaniaList.as_view(), name=views.AdresyZamieszkaniaList.name),
    path('adresyzamieszkania-detail/<int:pk>', views.AdresyZamieszkaniaDetail.as_view(), name=views.AdresyZamieszkaniaDetail.name),

    # ZarobkiURL
    path('zarobki-list', views.ZarobkiList.as_view(), name=views.ZarobkiList.name),
    path('zarobki-detail/<int:pk>', views.ZarobkiDetail.as_view(), name=views.ZarobkiDetail.name),

    # StatusDostawcyURL
    path('statusdostawcy-list', views.StatusDostawcyList.as_view(), name=views.StatusDostawcyList.name),
    path('statusdostawcy-detail/<int:pk>', views.StatusDostawcyDetail.as_view(), name=views.StatusDostawcyDetail.name),

    # DostawcyURL
    path('dostawcy-list', views.DostawcyList.as_view(), name=views.DostawcyList.name),
    path('dostawcy-detail/<int:pk>', views.DostawcyDetail.as_view(), name=views.DostawcyDetail.name),

    # DanePlatnosciURL
    path('daneplatnosci-list', views.DanePlatnosciList.as_view(), name=views.DanePlatnosciList.name),
    path('daneplatnosci-detail/<int:pk>', views.DanePlatnosciDetail.as_view(), name=views.DanePlatnosciDetail.name),

    # ZamowieniaURL
    path('zamowienia-list', views.ZamowieniaList.as_view(), name=views.ZamowieniaList.name),
    path('zamowienia-detail/<int:pk>', views.ZamowieniaDetail.as_view(), name=views.ZamowieniaDetail.name),

    # RestouracjeURL
    path('restouracje-list', views.RestouracjeList.as_view(), name=views.RestouracjeList.name),
    path('restouracje-detail/<int:pk>', views.RestouracjeDetail.as_view(), name=views.RestouracjeDetail.name),

    # ProduktyURL
    path('produkty-list', views.ProduktyList.as_view(), name=views.ProduktyList.name),
    path('produkty-detail/<int:pk>', views.ProduktyDetail.as_view(), name=views.ProduktyDetail.name),

    # AdresyRestouracjiURL
    path('adresyrestouracji-list', views.AdresyRestouracjiList.as_view(), name=views.AdresyRestouracjiList.name),
    path('adresyrestouracji-detail/<int:pk>', views.AdresyRestouracjiDetail.as_view(), name=views.AdresyRestouracjiDetail.name),





    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
urlpatterns = format_suffix_patterns(urlpatterns)