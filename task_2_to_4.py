import re

def count_russian_chars(s):
    return len(re.findall(r'[а-яА-ЯёЁ]', s))

def main():
    while True:
        c = input("\n1 - Русские символы, 0 - Выход\nВыбор: ")
        if c == '1': print("Русских символов:", count_russian_chars(input("Строка: ")))
        elif c == '0': break

if __name__ == "__main__": main()