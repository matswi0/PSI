from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    # DaneKontaktoweURL
    path('dane_kontaktowe/', views.DaneKontaktoweList.as_view()),
    path('dane_kontaktowe/<int:pk>/', views.DaneKontaktoweDetail.as_view()),

    # AdresDostawyURL
    path('adres_dostawy/', views.AdresDostawyList.as_view()),
    path('adres_dostawy/<int:pk>/', views.AdresDostawyDetail.as_view()),

    # KlienciURL
    path('klienci/', views.KlienciList.as_view()),
    path('klienci/<int:pk>/', views.KlienciDetail.as_view()),

    # AdresyZamieszkaniaURL
    path('adresy_zamieszkania/', views.AdresyZamieszkaniaList.as_view()),
    path('adresy_zamieszkania/<int:pk>/', views.AdresyZamieszkaniaDetail.as_view()),

    # ZarobkiURL
    path('zarobki/', views.ZarobkiList.as_view()),
    path('zarobki/<int:pk>/', views.ZarobkiDetail.as_view()),

    # StatusDostawcyURL
    path('status_dostawcy/', views.StatusDostawcyList.as_view()),
    path('status_dostawcy/<int:pk>/', views.StatusDostawcyDetail.as_view()),

    # DostawcyURL
    path('dostawcy/', views.DostawcyList.as_view()),
    path('dostawcy/<int:pk>/', views.DostawcyDetail.as_view()),

    # DanePlatnosciURL
    path('dane_platnosci/', views.DanePlatnosciList.as_view()),
    path('dane_platnosci/<int:pk>/', views.DanePlatnosciDetail.as_view()),

    # ZamowieniaURL
    path('zamowienia/', views.ZamowieniaList.as_view()),
    path('zamowienia/<int:pk>/', views.ZamowieniaDetail.as_view()),

    # RestouracjeURL
    path('restouracje/', views.RestouracjeList.as_view()),
    path('restouracje/<int:pk>/', views.RestouracjeDetail.as_view()),

    # ProduktyURL
    path('produkty/', views.ProduktyList.as_view()),
    path('produkty/<int:pk>/', views.ProduktyDetail.as_view()),

    # AdresyRestouracjiURL
    path('adresy_restouracji/', views.AdresyRestouracjiList.as_view()),
    path('adresy_restouracji/<int:pk>/', views.AdresyRestouracjiDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)