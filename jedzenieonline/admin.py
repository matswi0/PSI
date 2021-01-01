from django.contrib import admin
from .models import DaneKontaktowe, Klienci, AdresDostawy, AdresyZamieszkania, Zarobki, StatusDostawcy,\
    Dostawcy, DanePlatnosci, Zamowienia, Restouracje, Produkty, AdresyRestouracji


admin.site.register(DaneKontaktowe)
admin.site.register(Klienci)
admin.site.register(AdresDostawy)
admin.site.register(Dostawcy)
admin.site.register(DanePlatnosci)
admin.site.register(AdresyZamieszkania)
admin.site.register(Zarobki)
admin.site.register(StatusDostawcy)
admin.site.register(Zamowienia)
admin.site.register(Restouracje)
admin.site.register(Produkty)
admin.site.register(AdresyRestouracji)
