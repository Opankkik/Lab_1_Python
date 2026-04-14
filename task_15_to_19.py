def task_1_after_last_max(arr):
    if not arr: return 0
    return len(arr) - 1 - (len(arr) - 1 - arr[::-1].index(max(arr)))

def task_13_move_before_min(arr):
    if not arr: return []
    min_idx = arr.index(min(arr))
    return arr[min_idx:] + arr[:min_idx]

def main():
    arr = list(map(int, input("Массив (через пробел): ").split()))
    while True:
        c = input("\n1 - Элементы после последнего максимума, 2 - Элементы до минимального, 0-Выход\nВыбор: ")
        if c in ['1', '2']:
            if c == '1': print("Результат:", task_1_after_last_max(arr))
            elif c == '2': print("Результат:", task_13_move_before_min(arr))
        elif c == '0': break

if __name__ == "__main__": main()