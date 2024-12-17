# Get prime
def get_prime_number(max_limit=10000):
    primes = list()
    nums = 2
    while nums < max_limit:
        is_prime = True
        for i in primes:
            if nums % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums)
        nums += 1
    return primes


def get_fibonacci_numbers(max_limit=10000):
    fibos = list()
    F0 = FN_2 = 1
    F1 = FN_1 = 1
    while True:
        FN = FN_1 + FN_2
        if FN < max_limit:
            # print(FN)
            fibos.append(FN)
        else:
            break  # 強制跳出"迴圈"
        FN_1, FN_2 = FN, FN_1
    return fibos


if __name__ == "__main__":
    n = 100
    print(f"get prime number <{n}", get_prime_number(n))
    print(f"get fibonacci number <{n}", get_fibonacci_numbers(n))
