import re

def count_vowels_consonants_diff(s):
    v = len(re.findall(r'[aeiouаеёиоуыэюя]', s.lower()))
    c = len(re.findall(r'[bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ]', s.lower()))
    return abs(c - v)

def avg_ascii(s): return sum(ord(ch) for ch in s) / len(s) if s else 0

def cv_vc_diff(s):
    s_l = s.lower()
    vowels, cons = "aeiouаеёиоуыэюя", "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
    vc = sum(1 for i in range(len(s_l)-1) if s_l[i] in vowels and s_l[i+1] in cons)
    cv = sum(1 for i in range(len(s_l)-1) if s_l[i] in cons and s_l[i+1] in vowels)
    return abs(vc - cv)

def count_mirror_triplets(s):
    return sum(1 for i in range(len(s)-2) if s[i] == s[i+2]) / len(s) if s else 0

def main():
    lines = [x.strip() for x in input("Строки через запятую: ").split(',') if x.strip()]
    while True:
        c = input("\n1 - Сортировка по разнице согласных и гласных, 2 - Сортировка по отклонению ASCII, 3 - Сортировка по сочетанию гласных и согласных, 4 - Сортировка по среднему количеству зеркальных троек, 0-Выход\nВыбор: ")
        if c == '1': print(sorted(lines, key=count_vowels_consonants_diff))
        elif c == '2': base = avg_ascii(lines[0]); print(sorted(lines, key=lambda x: (avg_ascii(x) - base)**2))
        elif c == '3': print(sorted(lines, key=cv_vc_diff))
        elif c == '4': print(sorted(lines, key=count_mirror_triplets))
        elif c == '0': break

if __name__ == "__main__": main()