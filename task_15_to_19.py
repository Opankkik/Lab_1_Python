def task_1_after_last_max(arr):
    if not arr: return 0
    return len(arr) - 1 - (len(arr) - 1 - arr[::-1].index(max(arr)))

def task_13_move_before_min(arr):
    if not arr: return []
    min_idx = arr.index(min(arr))
    return arr[min_idx:] + arr[:min_idx]

def task_25_max_in_interval(arr, a, b):
    return max(arr[a:b+1]) if arr[a:b+1] else None

def task_37_less_than_left(arr):
    idx = [i for i in range(1, len(arr)) if arr[i] < arr[i-1]]
    return idx, len(idx)

def main():
    arr = list(map(int, input("Массив (через пробел): ").split()))
    while True:
        c = input("\n1 - Элементы после последнего максимума, 2 - Элементы до минимального, 3 - Максимальный элемент в интервале, 4 - Индексы элементов, меньших левого соседа, 0-Выход\nВыбор: ")
        if c in ['1', '2', '3', '4']:
            if c == '1': print("Результат:", task_1_after_last_max(arr))
            elif c == '2': print("Результат:", task_13_move_before_min(arr))
            elif c == '3':
                a, b = map(int, input("Интервал a и b (через пробел): ").split())
                print("Результат:", task_25_max_in_interval(arr, a, b))
            elif c == '4':
                idx, count = task_37_less_than_left(arr)
                print(f"Индексы: {idx}, Кол-во: {count}")
        elif c == '0': break

if __name__ == "__main__": main()