from django.db import models

class DaneKontaktowe(models.Model):
    numer_telefonu = models.CharField(max_length=9, null=False)
    adres_mailowy = models.EmailField(max_length=45, null=False)
    fax = models.CharField(max_length=7, null=True)


class AdresDostawy(models.Model):
    miejscowosc = models.CharField(max_length=45, null=False)
    kod_pocztowy = models.CharField(max_length=45, null=False)
    ulica = models.CharField(max_length=45, null=True)
    numer_domu = models.IntegerField(null=False)
    numer_lokalu = models.IntegerField(null=True)


class Klienci(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    dane_kontaktowe_id = models.ForeignKey(DaneKontaktowe, related_name='klienci', on_delete=models.CASCADE)
    adres_dostawy_id = models.ForeignKey(AdresDostawy, related_name='klienci', on_delete=models.CASCADE)

    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return self.imie+' '+self.nazwisko



class AdresyZamieszkania(models.Model):
    miejscowosc = models.CharField(max_length=45, null=False)
    kod_pocztowy = models.CharField(max_length=10, null=False)
    ulica = models.CharField(max_length=45, null=True)
    numer_domu = models.IntegerField(null=False)
    numer_lokalu = models.IntegerField(null=True)


class Zarobki(models.Model):
    okres_od = models.DateField(null=False)
    okres_do = models.DateField(null=False)
    przepracowane_godziny = models.IntegerField(null=False)
    stawka_godzinowa = models.IntegerField(null=False)


class StatusDostawcy(models.Model):
    rodzaj_umowy = models.CharField(max_length=20, null=False)
    numer_umowy = models.IntegerField(null=False)
    data_zatrudnienia = models.DateField(null=False)
    data_zwolnienia = models.DateField(null=True)
    koniec_umowy = models.DateField(null=False)
    dostepnosc_dostawcy = models.BooleanField()


class Dostawcy(models.Model):
    imie = models.CharField(max_length=20, null=False)
    nazwisko = models.CharField(max_length=20, null=False)
    pesel = models.CharField(max_length=11, null=False)
    dane_kontaktowe_id = models.ForeignKey(DaneKontaktowe, related_name='dostawcy', on_delete=models.CASCADE)
    adresy_zamieszkania_id = models.ForeignKey(AdresyZamieszkania, related_name='dostawcy', on_delete=models.CASCADE)
    status_dostawcy_id = models.ForeignKey(StatusDostawcy, related_name='dostawcy', on_delete=models.CASCADE)
    zarobk_id = models.ForeignKey(Zarobki,related_name='dostawcy', on_delete=models.CASCADE)
    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return self.imie+' '+self.nazwisko


class DanePlatnosci(models.Model):
    BLIK = 'BLIK'
    GOT = 'GOTÓWKA'
    PRZEL = 'PRZELEW'
    METODY_PLATNOSCI = ((BLIK, 'Blik'), (GOT, 'Przy odbiorze'), (PRZEL, 'Przelew'), )
    id_klient = models.ForeignKey(Klienci, related_name='dane_platnosci', on_delete=models.CASCADE)
    data_platnosci = models.DateField(null=False)
    metoda_platnosci = models.CharField(max_length=15, choices=METODY_PLATNOSCI, default=GOT)
    status_platnosci = models.BooleanField(null=False)


class Zamowienia(models.Model):
    klient_id = models.ForeignKey(Klienci, related_name='zamowienia', on_delete=models.CASCADE)
    dostawcy_id = models.ForeignKey(Dostawcy, related_name='zamowienia', on_delete=models.CASCADE)
    dane_platnosci_id = models.ForeignKey(DanePlatnosci, related_name='zamowienia', on_delete=models.CASCADE)
    status_zamowienia = models.BooleanField(null=False)


class Restouracje(models.Model):
    nazwa_restouracji = models.CharField(max_length=45, null=False)
    numer_telefonu = models.CharField(max_length=9, null=False)
    nip = models.CharField(max_length=12, null=False)
    class Meta:
        ordering = ('nazwa_restouracji',)

    def __str__(self):
        return self.nazwa_restouracji+' '+self.numer_telefonu



class Produkty(models.Model):
    PRODUKTY_CHOICES = (('PIZZA', 'pizza'), ('BURGER', 'burger'), ('KEBAB', 'kebab'), ('SUSHI', 'sushi'),)
    typ_produktu = models.CharField(max_length=10, choices=PRODUKTY_CHOICES, null=False)
    nazwa_produktu = models.CharField(max_length=45, null=False)
    cena = models.DecimalField(max_digits=14, decimal_places=2)
    restouracja_id = models.ForeignKey(Restouracje, related_name='produkty', on_delete=models.CASCADE)


class AdresyRestouracji(models.Model):
    miejscowosc = models.CharField(max_length=45, null=False)
    kod_pocztowy = models.CharField(max_length=6, null=False)
    ulica = models.CharField(max_length=45, null=True)
    numer_domu = models.IntegerField(null=False)
    numer_lokalu = models.IntegerField(null=True)
    restouracja_id = models.ForeignKey(Restouracje, related_name='adresy_restouracji', on_delete=models.CASCADE)