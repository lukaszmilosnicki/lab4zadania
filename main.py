# Zad 1
# liczba = 0
# liczby = [liczba for liczba in range(30) if liczba % 4 == 0]
# plik = open('podzielne.txt', 'w')
# plik.write(str(liczby))
# plik.close()
#
# Zad 2
# with open('podzielne.txt', 'r') as podzielne:
#     linie = podzielne.readlines()
#     print(linie)
#
# Zad 3
# with open('tekst.txt', 'w') as tekst:
#     t = ('Lorem Ipsum ' + '\n' + 'is simply dummy text of the printing' + '\n' + 'and typesetting industry.')
#     tekst.write(t)
# with open('tekst.txt', 'r') as x:
#     for linia in x:
#         print(linia, end="")
#
# Zad 4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         return self.nazwa_produktu
#     def ile_produktu(self):
#         return f'{self.ilosc} {self.jednostka_miary}'
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jed
#
# produkt = NaZakupy('ziemniaki', 5, 'kg', 2)
#
# print(produkt.wyswietl_produkt())
# print(produkt.ile_produktu())
# print(produkt.ile_kosztuje())