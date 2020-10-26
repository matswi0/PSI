import string
#zad 1
zmienna = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Szymon"
nazwisko = "Suchecki"

print("Zadanie 2")
print(f"W tekście jest   {zmienna.count(imie[1])} liter {imie[1]}   oraz  {zmienna.count(nazwisko[2])}   liter  {nazwisko[2]}")

#input()
# zad 4 .pomysl nad tym
#def zrob_cos():
#   return 'zrobione'
#zmienna_typu_string = "może być jako odwołanie do zmiennej lub bezpośrednio ciąg tekstowy"
#print(dir(zmienna_typu_string))
#help(zmienna_typu_string.zrob_cos)
print("Zadanie 5")
print(string.capwords(imie[::-1]) + " " + string.capwords(nazwisko[::-1]))
#input()

print("zadanie 6")
lista = [1,2,3,4,5,6,7,8,9,10]

lista1 = lista[:5]
lista2 = lista[5:]
print(lista1)
print(lista2)
#input()

print("Zadanie 7")
lista_polaczona = lista1 + lista2
lista_polaczona.insert(0,0)
print(lista_polaczona)
lista_odwrocona = lista_polaczona

lista_odwrocona.sort(reverse=True)
print(lista_odwrocona)
#input()

print("Zadanie 8")

numer_indeksu = (143123, 154123, 156212)
imie_nazwisko = ("Szymon Suchecki", "Mateusz Świderski", "Klocuch12")

print(numer_indeksu)
print(imie_nazwisko)

lista_studentow = numer_indeksu + imie_nazwisko

print(lista_studentow)

slownik = {}

slownik = {
    143123 : "Szymon Suchecki",
    154123 : "Mateusz Świderski",
    156212 : "Klocuch12"
}
print(slownik)

slownik.setdefault('wiek', )
