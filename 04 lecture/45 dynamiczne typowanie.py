# co to znaczy że python jest językiem dynamicznie typowanym

# to zaczy że typy są przydzielne do zmiennych dynamicznie - oznacza to że typ danych można zmieniać w czasie istnienia zmiennej

# statyczne typowanie w pythonie pozala poinformować innych użytkownuków kodu czym ma być konkretna zmienna

# a=5
# print(type(a))
# a='pięć'
# print(type(a))



from typing import List

def przeliteruj(word: str) -> List[str]: # ten mechanizm nazywa się type hints
    return list(word)

print(przeliteruj())
# konsola nie zwróci błędów nawet jeśli wprowadzi się typ danych inny niż string.
# aby zobaczyć te błędy trzeba zainstalować dodatkową bibliotekę mypy i w terminalu użyć komenty mypy + nazwa pliku