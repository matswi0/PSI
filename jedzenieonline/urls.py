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

    # DostawcyURL
    path('dostawcy-list', views.DostawcyList.as_view(), name=views.DostawcyList.name),
    path('dostawcy-detail/<int:pk>', views.DostawcyDetail.as_view(), name=views.DostawcyDetail.name),

    # DanePlatnosciURL
    path('daneplatnosci-list', views.DanePlatnosciList.as_view(), name=views.DanePlatnosciList.name),
    path('daneplantosci-detail/<int:pk>', views.DanePlatnosciDetail.as_view(), name=views.DanePlatnosciDetail.name),

    # ZamowieniaURL
    path('zamowienia-list', views.ZamowieniaList.as_view(), name=views.ZamowieniaList.name),
    path('zamowienia-detail/<int:pk>', views.ZamowieniaDetail.as_view(), name=views.ZamowieniaDetail.name),

    # RestauracjeURL
    path('restauracje-list', views.RestauracjeList.as_view(), name=views.RestauracjeList.name),
    path('restauracje-detail/<int:pk>', views.RestauracjeDetail.as_view(), name=views.RestauracjeDetail.name),

    # ProduktyURL
    path('produkty-list', views.ProduktyList.as_view(), name=views.ProduktyList.name),
    path('produkty-detail/<int:pk>', views.ProduktyDetail.as_view(), name=views.ProduktyDetail.name),

    # AdresyRestauracjiURL
    path('adresyrestauracji-list', views.AdresyRestauracjiList.as_view(), name=views.AdresyRestauracjiList.name),
    path('adresyrestauracji-detail/<int:pk>', views.AdresyRestauracjiDetail.as_view(), name=views.AdresyRestauracjiDetail.name),

    # UserURL
    path('user-list', views.UserList.as_view(), name=views.UserList.name),
    path('user-detail/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),


    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
urlpatterns = format_suffix_patterns(urlpatterns)