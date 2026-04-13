import re

def max_real_number(s):
    nums = re.findall(r'-?\d+\.\d+|-?\d+', s)
    return max(map(float, nums)) if nums else None

def min_rational_number(s):
    nums = re.findall(r'-?\d+\.\d+|-?\d+', s)
    return min(map(float, nums)) if nums else None

def max_consecutive_digits(s):
    seqs = re.findall(r'\d+', s)
    return max(len(seq) for seq in seqs) if seqs else 0

def main():
    while True:
        c = input("\n1 - Макс. веществ., 2 - Мин. рацион., 3 - Подряд цифры, 0 - Выход\nВыбор: ")
        if c == '1': print("Результат:", max_real_number(input("Строка: ")))
        elif c == '2': print("Результат:", min_rational_number(input("Строка: ")))
        elif c == '3': print("Результат:", max_consecutive_digits(input("Строка: ")))
        elif c == '0': break

if __name__ == "__main__": main()