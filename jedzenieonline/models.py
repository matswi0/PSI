from django.db import models

class DaneKontaktowe(models.Model):
    numer_telefonu = models.IntegerField(null=False)
    adres_mailowy = models.CharField(max_length=45, null=False)
    fax = models.IntegerField(null=True)


class AdresDostawy(models.Model):
    miejscowosc = models.CharField(max_length=45, null=False)
    kod_pocztowy = models.CharField(max_length=45, null=False)
    ulica = models.CharField(max_length=45, null=True)
    numer_domu = models.IntegerField(null=False)
    numer_lokalu = models.IntegerField(null=False)


class Klienci(models.Model):
    imie = models.IntegerField(null=False)
    nazwisko = models.IntegerField(null=False)
    dane_kontaktowe_id = models.ForeignKey(DaneKontaktowe, on_delete=models.CASCADE)
    adres_dostawy_id = models.ForeignKey(AdresDostawy, on_delete=models.CASCADE)


class AdresyZamieszkania(models.Model):
    miejscowosc = models.CharField(max_length=45, null=False)
    kod_pocztowy = models.CharField(max_length=45, null=False)
    ulica = models.CharField(max_length=45, null=True)
    numer_domu = models.IntegerField(null=False)
    numer_lokalu = models.IntegerField(null=False)


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
    dostepnosc_dostawcy = models.BooleanField(null=False)


class Dostawcy(models.Model):
    imie = models.IntegerField(null=False)
    nazwisko = models.IntegerField(null=False)
    pesel = models.IntegerField(null=False)
    dane_kontaktowe_id = models.ForeignKey(DaneKontaktowe, on_delete=models.CASCADE)
    adresy_zamieszkania_id = models.ForeignKey(AdresyZamieszkania, on_delete=models.CASCADE)
    status_dostawcy_id = models.ForeignKey(StatusDostawcy, on_delete=models.CASCADE)
    zarobk_id = models.ForeignKey(Zarobki, on_delete=models.CASCADE)



class DanePlatnosci(models.Model):
    id_klienta = models.ForeignKey(Klienci, on_delete=models.CASCADE)
    data_platnosci = models.DateField(null=False)
    metoda_platnosci = models.CharField(max_length=15, null=False)
    status_platnosci = models.CharField(max_length=15, null=False)


class Zamowienia(models.Model):
    dostawcy_id = models.ForeignKey(Dostawcy, on_delete=models.CASCADE)
    dane_platnosci_id = models.ForeignKey(DanePlatnosci, on_delete=models.CASCADE)
    status_zamowienia = models.BooleanField(null=False)


class Restouracje(models.Model):
    nazwa_restouracji = models.CharField(max_length=45, null=False)
    numer_telefonu = models.IntegerField(null=False)
    nip = models.IntegerField(null=False)


class Produkty(models.Model):
    typ_produktu = models.CharField(max_length=15, null=False)
    nazwa_produktu = models.CharField(max_length=45, null=False)
    cena = models.IntegerField(null=False)
    nazwa_produktu = models.CharField(max_length=300, null=False)
    restouracja_id = models.ForeignKey(Restouracje, on_delete=models.CASCADE)


class AdresyRestouracji(models.Model):
    restouracja_id = models.ForeignKey(Restouracje, on_delete=models.CASCADE)
    miejscowosc = models.CharField(max_length=45, null=False)
    kod_pocztowy = models.CharField(max_length=45, null=False)
    ulica = models.CharField(max_length=45, null=True)
    numer_domu = models.IntegerField(null=False)
    numer_lokalu = models.IntegerField(null=False)