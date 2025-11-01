import random

def main():
    # Tworzenie dwóch list do połączenia funkcją zip()
    # Dokumentacja zip(): https://docs.python.org/3/library/functions.html#zip
    imiona = ['Anna', 'Jan', 'Ewa', 'Piotr', 'Maria']
    wiek = [25, 30, 28, 35, 32]
    
    print("Lista 1 (imiona):", imiona)
    print("Lista 2 (wiek):", wiek)
    
    # Łączenie list funkcją zip() - tworzy pary (imię, wiek)
    polaczone = zip(imiona, wiek)
    
    # Konwersja na listę krotek i wyświetlenie wyniku
    lista_polaczona = list(polaczone)
    print("\nPołączone listy (zip):", lista_polaczona)
    
    # Wykorzystanie funkcji z modułu random
    # Dokumentacja random: https://docs.python.org/3/library/random.html
    print("\n--- Użycie modułu random ---")
    
    # Losowy wybór imienia z listy za pomocą random.choice()
    wylosowane_imie = random.choice(imiona)
    print(f"Wylosowane imię: {wylosowane_imie}")
    
    # Losowanie liczby z zakresu 1-100
    wylosowana_liczba = random.randint(1, 100)
    print(f"Wylosowana liczba (1-100): {wylosowana_liczba}")
    
    # Obsługa wyjątków - przykład z ValueError
    # Dokumentacja ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    print("\n--- Obsługa wyjątków ---")
    
    # Próba konwersji nieprawidłowego stringa na liczbę całkowitą
    testowe_dane = ['123', '45.67', 'abc', '789']
    
    for dane in testowe_dane:
        try:
            # Próba konwersji stringa na int
            liczba = int(dane)
            print(f"Konwersja '{dane}' na int: {liczba}")
            
        except ValueError as e:
            # Obsługa wyjątku ValueError - nieprawidłowa wartość dla int()
            print(f"Błąd ValueError dla '{dane}': {e}")
            print("To nie jest prawidłowa liczba całkowita!")
            
        except Exception as e:
            # Ogólna obsługa innych wyjątków
            print(f"Inny błąd dla '{dane}': {e}")
    
    # Dodatkowy przykład z ZeroDivisionError
    print("\n--- Dodatkowy przykład z dzieleniem przez zero ---")
    
    try:
        licznik = 10
        mianownik = 0
        wynik = licznik / mianownik
        print(f"Wynik dzielenia: {wynik}")
        
    except ZeroDivisionError as e:
        print(f"Błąd ZeroDivisionError: {e}")
        print("Nie można dzielić przez zero!")
    
    print("\nProgram zakończony pomyślnie!")

if __name__ == "__main__":
    main()