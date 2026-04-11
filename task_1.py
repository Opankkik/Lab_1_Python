# Задание 1.1: Сумма простых делителей
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def sum_prime_divisors(n):
    sum_res = 0
    for i in range(2, abs(n) + 1):
        if n % i == 0 and is_prime(i):
            sum_res += i
    return sum_res

if __name__ == "__main__":
    num = int(input("Введите число для задачи 1.1: "))
    print(f"Сумма простых делителей: {sum_prime_divisors(num)}")

# Задание 1.2: Количество нечетных цифр, больших 3
def count_odd_digits_greater_than_3(n):
    count = 0
    for digit in str(abs(n)):
        d = int(digit)
        if d % 2 != 0 and d > 3:
            count += 1
    return count

if __name__ == "__main__":
    num2 = int(input("Введите число для задачи 1.2: "))
    print(f"Нечетных цифр > 3: {count_odd_digits_greater_than_3(num2)}")