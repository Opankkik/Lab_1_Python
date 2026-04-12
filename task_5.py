import re

def find_text_dates(s):
    pattern = r'\b\d{1,2}\s+(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+\d{4}\b'
    return re.findall(pattern, s, re.IGNORECASE)

if __name__ == "__main__":
    s = input("Введите строку для поиска дат: ")
    print("Найденные даты:", find_text_dates(s))