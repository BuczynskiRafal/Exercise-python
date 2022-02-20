# Pytanie 41 - napisz funkcję, która dla podanego katalgu wypisze znajdujące się w nim pliki.
# Pamiętaj, że katalog może zawierać podkatalogi, do których funkcja również musi zajrzeć.

# os.listdir - zwraca zawartość danego katalogu
# os.path.join - łączy dwa stringi w ścieżkę czytelną dla danego systemu operacyjnego
# os.path.isdir - sprawdza czy podana ściezka jest katalogiem

import os

ROOT = r'D:\Users\rbuczynski\Documents\GitHub\Exercise-python'

def list_patch(root):
    for element in os.listdir(root):
        element_root = os.path.join(root, element)
        if os.path.isdir(element_root):
            list_patch(element_root)
        else:
            print(element_root)

def wypisz_zawartosc_katalogu(ROOT):
    for element in os.listdir(ROOT):        # dla każdego elementu w katalogu pod adresem 'sciezka_do_katalogu'
        sciezka_do_elementu = os.path.join(ROOT, element) # przy uzyciu os.path.join utworz sciezke do tego elementu
        if os.path.isdir(sciezka_do_elementu):             # jeśli element jest również katalogiem
            wypisz_zawartosc_katalogu(sciezka_do_elementu) # uruchom rekurencyjnie funkcję wypisz_zawartosc_katalogu z adresem elementu jako argumentem
        else:                                              # w przeciwnym wypadku (czyli element nie jest katalogiem)
            print(sciezka_do_elementu)                     # wypisz element

print(list_patch(ROOT))
print(wypisz_zawartosc_katalogu(ROOT))