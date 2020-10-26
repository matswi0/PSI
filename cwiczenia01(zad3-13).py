from datetime import datetime
import string
def zad3():
    print('{:_>10}'.format('test hgheh'))
    print('{first} {last}'.format(first='Pierwszy', last='Ostatni'))
    print('{:%Y-%m-%d %H:%M}'.format(datetime(2020, 10, 26, 20, 44)))
    print('{:{align}{width}}'.format('test', align='^', width='100'))

    class Klasa(object):

        def __format__(self, format_spec):
            if (format_spec == 'Ja jestem kibicem lecha'):
                return "Uhuhu"
            return 'Klasa'
    print('{:Ja jestem kibicem lecha}'.format(Klasa()))
#zad3()

def zad4():
    zmienna_typu_string = "zmienna typu string"
    help(zmienna_typu_string.upper())
#zad4()

def zad5():
    imie = "Mateusz"
    nazwisko = "Świderski"
    print(string.capwords(imie[::-1]) + " " + string.capwords(nazwisko[::-1]))
#zad5()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1 = lista[:5]
lista2 = lista[5:]

def zad6():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista1 = lista[:5]
    lista2 = lista[5:]
    print(lista1)
    print(lista2)
#zad6()

def zad7(lista1, lista2):
    lista = lista1 + lista2
    lista.insert(0, 0)
    print(lista)
    lista_kopia = lista
    lista_kopia.sort(reverse=True)
    print(lista_kopia)
#zad7(lista1, lista2)

imie_nazwisko = ("Mateusz Świderski", "Szymon Suchecki")
numer_indeksu = ("150514", "151376")

def zad8(imie_nazwisko, numer_indeksu):
    for i in range(len(numer_indeksu)):
        print(numer_indeksu[i] + " " + imie_nazwisko[i])
#zad8(imie_nazwisko, numer_indeksu)

def zad9(imie_nazwisko, numer_indeksu):
    slownik = {}
    for i in range(len(imie_nazwisko)):
        slownik[numer_indeksu[i]] = imie_nazwisko[i]
    for i, j in slownik.items():
        print(i, j)
#zad9(imie_nazwisko, numer_indeksu)

def zad10():
    numerytel = ["534231092", "888222333", "777222333", "534231092"]
    bezpowt = set(numerytel)
    print(bezpowt)
#zad10()

def zad11():
    for i in range(1, 11):
        print(i)
#zad11()

def zad12():
    for i in reversed(range(20, 101, 5)):
        print(i)
#zad12()

def zad13():
    lista = [{"wart1": "klucz1"}, {"wart2": "klucz2"}, {"wart3": "klucz3"}]
    for elem in lista:
        for i, j in elem.items():
            print(i, j)
#zad13()