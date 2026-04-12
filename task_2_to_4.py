import re

def count_russian_chars(s):
    return len(re.findall(r'[а-яА-ЯёЁ]', s))

def is_latin_lower_palindrome(s):
    letters = re.findall(r'[a-z]', s)
    return letters == letters[::-1] and len(letters) > 0

def find_dates(s):
    return re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', s)

def main():
    while True:
        c = input("\n1 - Русские символы, 2 - Палиндром, 3 - Даты, 0 - Выход\nВыбор: ")
        if c == '1': print("Русских:", count_russian_chars(input("Строка: ")))
        elif c == '2': print("Палиндром:", is_latin_lower_palindrome(input("Строка: ")))
        elif c == '3': print("Даты:", find_dates(input("Строка: ")))
        elif c == '0': break

if __name__ == "__main__": main()