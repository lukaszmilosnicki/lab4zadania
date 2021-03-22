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