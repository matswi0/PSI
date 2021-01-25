from django.contrib import admin
from .models import DaneKontaktowe, Klienci, AdresDostawy, AdresyZamieszkania,\
    Dostawcy, DanePlatnosci, Zamowienia, Restauracje, Produkty, AdresyRestauracji


admin.site.register(DaneKontaktowe)
admin.site.register(Klienci)
admin.site.register(AdresDostawy)
admin.site.register(Dostawcy)
admin.site.register(DanePlatnosci)
admin.site.register(AdresyZamieszkania)
admin.site.register(Zamowienia)
admin.site.register(Restauracje)
admin.site.register(Produkty)
admin.site.register(AdresyRestauracji)
