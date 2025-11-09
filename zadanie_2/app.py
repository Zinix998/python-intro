def validate_email(email):
    if not email or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local_part, domain = parts
    
    if not local_part or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True


def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    
    return 3.14159 * radius ** 2


def filter_even_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input musi być listą")
    
    return [num for num in numbers if isinstance(num, (int, float)) and num % 2 == 0]


def convert_date_format(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Data musi być stringiem")
    
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Niepoprawny format daty. Oczekiwano: RRRR-MM-DD")
    
    year, month, day = parts
    
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("Niepoprawny format daty. Oczekiwano: RRRR-MM-DD")
    
    return f"{day}.{month}.{year}"


def is_palindrome(text):
    if not isinstance(text, str):
        return False
    
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    return cleaned_text == cleaned_text[::-1]