import math
a_list = ['1', '2', '3']
b_list = ['4', '5', '6']
def zadanie1(a_list, b_list):
    for i, j in enumerate(a_list):
        b_list.insert(2 * i + 1, j)
    return b_list
#print(zadanie1(a_list, b_list))

data_text = "Dog"


def zadanie2(data_text):
    dict = {
        "length": "",
        "letters": "",
        "big_letters": "",
        "small_letters": ""
    }
    dict["length"] = len(data_text)
    dict["letters"] = list(data_text)
    dict["big_letters"] = data_text.upper()
    dict["small_letters"] = data_text.lower()
    return dict
#print(zadanie2(data_text))

letter = "b"
text = "basia"
def zadanie3(letter, text):
    text = text.replace(letter, "")
    return text
#print(zadanie3(letter, text))

def zadanie4(celsjusz, temperature_type):
    if isinstance(celsjusz, float) or isinstance(celsjusz, int):
        if temperature_type == 'K':
            print("Kelvin:{0}".format(celsjusz + 273.15))
        elif temperature_type == 'F':
            print("Fahrenheit:{0}".format(celsjusz * 1.8 + 32))
        elif temperature_type == 'R':
            print("Rankine:{0}".format((celsjusz + 273.15) * 1.8))
        else:
            print("Dane są nieprawidłowe!")
    else:
        print("Dane są nieprawidłowe!")
zadanie4(32,'R')


class Calculator:
    def __init__(self, f, s):
        self.a = f
        self.b = s
    def add(self):
        return self.a + self.b
    def difference(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

class ScienceCalculator(Calculator):
    def Potegowanie(self):
        return pow(self.a,self.b)
    def Pierwiastek(self):
        return math.sqrt(self.a+self.b)

operacja = Calculator(2, 3)
print(f"{operacja.multiply()}")
print(f"{operacja.divide()}")

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name
    def update_file(self, text_data):
        plik = open(self.file_name, 'a', encoding='utf-8')
        plik.write(text_data)
    #(nie potrafiłem zrobić)def read_file(self):


plik1 = FileManager('plik.txt')


def zadanie7(text):
    print(text[::-1])
#zadanie7("koteł")