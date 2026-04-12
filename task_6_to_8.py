import re

def max_real_number(s):
    numbers = re.findall(r'-?\d+\.\d+|-?\d+', s)
    return max(map(float, numbers)) if numbers else None

def main():
    while True:
        c = input("\n1 - Макс. вещественное, 0 - Выход\nВыбор: ")
        if c == '1': print("Результат:", max_real_number(input("Строка: ")))
        elif c == '0': break

if __name__ == "__main__": main()