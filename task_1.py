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