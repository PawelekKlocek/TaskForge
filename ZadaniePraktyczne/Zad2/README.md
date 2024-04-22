
# Zadanie 2

## Opis zadania

Zadanie polega na rozbudowaniu kodu z poprzedniego zadania o mechanizm flashowania, który będzie informował użytkownika o błędach, 
gdy nazwa użytkownika nie spełnia określonych kryteriów. Gdy nazwa użytkownika jest poprawna, użytkownik zostanie przekierowany do strony powitalnej, 
gdzie wyświetli się komunikat "Witaj, [imię użytkownika]!".

### Krok 1: Rozszerzenie kodu
Otwórz plik app.py z poprzedniego zadania i dodaj mechanizm flashowania w przypadku, gdy nazwa użytkownika jest za krótka lub nie zaczyna się od dużej litery.
Skorzystaj z funkcji flash z modułu Flask. Upewnij się, że po poprawnej walidacji nazwy użytkownika użytkownik zostanie przekierowany do strony /welcome.

### Krok 2: Utworzenie strony powitalnej
Utwórz szablon HTML o nazwie welcome.html.
W szablonie wyświetl komunikat "Witaj, [imię użytkownika]!", gdzie [imię użytkownika] będzie zmienną zawierającą poprawną nazwę użytkownika.

