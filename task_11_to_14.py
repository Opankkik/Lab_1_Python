import re

def count_vowels_consonants_diff(s):
    s_lower = s.lower()
    vowels = len(re.findall(r'[aeiouаеёиоуыэюя]', s_lower))
    consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ]', s_lower))
    return abs(consonants - vowels)

def main():
    lines = [x.strip() for x in input("Введите строки через запятую: ").split(',') if x.strip()]
    if not lines: return
    while True:
        c = input("\n1 - Сорт. разница согл/гл, 0 - Выход\nВыбор: ")
        if c == '1': print(sorted(lines, key=count_vowels_consonants_diff))
        elif c == '0': break

if __name__ == "__main__": main()