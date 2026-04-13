def task_1_after_last_max(arr):
    if not arr: return 0
    last_max_idx = len(arr) - 1 - arr[::-1].index(max(arr))
    return len(arr) - 1 - last_max_idx

def main():
    arr = list(map(int, input("Массив (через пробел): ").split()))
    while True:
        c = input("\n1 - Элементы после последнего макс., 0 - Выход\nВыбор: ")
        if c == '1':
            print("Результат:", task_1_after_last_max(arr))
        elif c == '0': break

if __name__ == "__main__": main()