from django.db import models

class DaneKontaktowe(models.Model):
    numer_telefonu = models.CharField(max_length=9, null=False)
    adres_mailowy = models.EmailField(max_length=45, null=False)
    fax = models.CharField(max_length=7, null=True)
    def __str__(self):
        return self.numer_telefonu


class AdresDostawy(models.Model):
    miejscowosc = models.CharField(max_length=45, null=False)
    kod_pocztowy = models.CharField(max_length=45, null=False)
    ulica = models.CharField(max_length=45, null=True)
    numer_domu = models.IntegerField(null=False)
    numer_lokalu = models.IntegerField(null=True)

    def __str__(self):
        return self.miejscowosc + ' ' + self.ulica + ' ' + str(self.numer_domu) + ' / ' + str(self.numer_lokalu)


class Klienci(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    dane_kontaktowe_id = models.ForeignKey(DaneKontaktowe, related_name='klienci', on_delete=models.CASCADE)
    adres_dostawy_id = models.ForeignKey(AdresDostawy, related_name='klienci', on_delete=models.CASCADE)
    wlasciciel = models.ForeignKey('auth.User', related_name='klienci', on_delete=models.CASCADE)
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

    def __str__(self):
        return self.miejscowosc + ' ' +self.ulica + ' ' +str(self.numer_domu) + ' / ' + str(self.numer_lokalu)


class Dostawcy(models.Model):
    imie = models.CharField(max_length=20, null=False)
    nazwisko = models.CharField(max_length=20, null=False)
    pesel = models.CharField(max_length=11, null=False)
    numer_umowy = models.IntegerField(null=False)
    dostepnosc_dostawcy = models.BooleanField()
    dane_kontaktowe_id = models.ForeignKey(DaneKontaktowe, related_name='dostawcy', on_delete=models.CASCADE)
    adresy_zamieszkania_id = models.ForeignKey(AdresyZamieszkania, related_name='dostawcy', on_delete=models.CASCADE)
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


class Restauracje(models.Model):
    nazwa_restauracji = models.CharField(max_length=45, null=False)
    numer_telefonu = models.CharField(max_length=9, null=False)
    nip = models.CharField(max_length=12, null=False)
    class Meta:
        ordering = ('nazwa_restauracji',)

    def __str__(self):
        return self.nazwa_restauracji+' '+self.numer_telefonu



class Produkty(models.Model):
    PRODUKTY_CHOICES = (('PIZZA', 'pizza'), ('BURGER', 'burger'), ('KEBAB', 'kebab'), ('SUSHI', 'sushi'),)
    typ_produktu = models.CharField(max_length=10, choices=PRODUKTY_CHOICES, null=False)
    nazwa_produktu = models.CharField(max_length=45, null=False)
    cena = models.DecimalField(max_digits=14, decimal_places=2)
    restauracja_id = models.ForeignKey(Restauracje, related_name='produkty', on_delete=models.CASCADE)
    wlasciciel = models.ForeignKey('auth.User', related_name='produkty', on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa_produktu

class AdresyRestauracji(models.Model):
    miejscowosc = models.CharField(max_length=45, null=False)
    kod_pocztowy = models.CharField(max_length=6, null=False)
    ulica = models.CharField(max_length=45, null=True)
    numer_domu = models.IntegerField(null=False)
    numer_lokalu = models.IntegerField(null=True)
    restauracja_id = models.ForeignKey(Restauracje, related_name='adresy_restauracji', on_delete=models.CASCADE)

    def __str__(self):
        return self.miejscowosc + ' ' + self.ulica + ' ' + str(self.numer_domu) + ' / ' + str(self.numer_lokalu)

