import random
import math
import time

from arithmetic import modular_pow

# a test value for different n
# n <               2 047 : [2]
# n <           1 373 653 : [2, 3]
# n <           9 080 191 : [31, 73]
# n <          25 326 001 : [2, 3, 5]
# n <       3 215 031 751 : [2, 3, 5, 7]
# n <       4 759 123 141 : [2, 7, 61]
# n <   1 122 004 669 633 : [2, 13, 23, 1662803]
# n <   2 152 302 898 747 : [2, 3, 5, 7, 11]
# n <   3 474 749 660 383 : [2, 3, 5, 7, 11, 13]
# n < 341 550 071 728 321 : [2, 3, 5, 7, 11, 13, 17]
# 2**32     4 294 967 296   for reference
# More values at: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller_test
# More trickery at: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n

def naive_prime(n):
    if n < 2:
        return False
    for i in range(2, min(n, int(math.sqrt(n)) + 1)):
        if n % i == 0:
            return False
    return True

global a_values
a_values = [2, 7, 61]
def miller_test(n):
    if n < 2 or n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d = d // 2
    for a in a_values:
        x = modular_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        should_continue = False
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                should_continue = True
                break
        if should_continue:
            continue
        return False
    return True


def find_prime_up_to_n(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False
    for i in range(2, n + 1):
        if not is_prime[i]:
            continue
        current = i * 2
        while current <= n:
            is_prime[current] = False
            current += i
    primes = set()
    for i, value in enumerate(is_prime):
        if value:
            primes.add(i)
    return primes


if __name__ == '__main__':
    amount = 10000
    # max_number = 4759123140
    # a_values = [2, 7, 61]
    # 25 326 001 : [2, 3, 5]
    max_number = 25326001
    a_values = [2, 3, 5]
    inputs = [random.randint(2, max_number) for _ in range(amount)]

    start = time.time()
    naive_answers = [naive_prime(x) for x in inputs]
    naive_time = time.time() - start
    print(f"Naive took {1000 * naive_time / amount} ms per number")

    start = time.time()
    miller_answers = [miller_test(x) for x in inputs]
    miller_time = time.time() - start
    print(f"Miller took {1000 * miller_time / amount} ms per number")

    start = time.time()
    all_primes = find_prime_up_to_n(max_number)
    find_all_time = time.time() - start
    print(f"Finding all primes took {find_all_time} seconds")

    start = time.time()
    lookup_answers = [x in all_primes for x in inputs]
    lookup_time = time.time() - start
    print(f"Lookup took {1000 * lookup_time / amount} ms per number")

    print(f"There needs to be at least {find_all_time * amount / (miller_time - lookup_time)} checks for precomputing to be worth it")
    # find_all_time + queries * lookup_single_time = queries * miller_single_time
    # queries * (miller_single_time - lookup_single_time) = find_all_time
    # queries * (miller_time - lookup_time) / amount = find_all_time
    # queries = find_all_time * amount / (miller_time - lookup_time)
