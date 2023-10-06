import random
import math


from disjoint_subsets import DisjointSubsets


def is_prime(number):
    for i in range(2, min(number, int(math.sqrt(number)) + 2)):
        if number % i == 0:
            return False
    return True

def randomize_order(a, b):
    if random.getrandbits(1):
        return a, b
    return b, a


def test_disjoint_subsets_with_random_primes():
    primes = []
    non_primes = []
    sets = DisjointSubsets()
    for i in range(10000):
        number = random.randint(2, 10000)
        data = "-".join([x for x in str(number)])
        if is_prime(number):
            if len(primes) > 0:
                some_other = random.choice(primes)
            primes.append(number)
            sets.add_with_check(number, data)
            if len(primes) > 1:
                a, b = randomize_order(number, some_other)
                sets.join(a, b)
        else:
            if len(non_primes) > 0:
                some_other = random.choice(non_primes)
            non_primes.append(number)
            sets.add_with_check(number, data)
            if len(non_primes) > 1:
                a, b = randomize_order(number, some_other)
                sets.join(a, b)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(non_primes)
        b = random.choice(non_primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(non_primes)
        assert not sets.in_same(a, b)

def test_disjoint_subsets_with_consecutive_primes():
    primes = []
    non_primes = []
    sets = DisjointSubsets()
    for i in range(2, 10000):
        number = i
        data = "-".join([x for x in str(number)])
        if is_prime(number):
            if len(primes) > 0:
                some_other = random.choice(primes)
            primes.append(number)
            sets.add(number, data)
            if len(primes) > 1:
                sets.join(number, some_other)
        else:
            if len(non_primes) > 0:
                some_other = random.choice(non_primes)
            non_primes.append(number)
            sets.add(number, data)
            if len(non_primes) > 1:
                sets.join(number, some_other)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(non_primes)
        b = random.choice(non_primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(non_primes)
        assert not sets.in_same(a, b)

def test_disjoint_subsets_with_random_primes_that_dont_all_exist():
    primes = []
    non_primes = []
    sets = DisjointSubsets()
    for i in range(1000):
        number = random.randint(2, 10000)
        data = "-".join([x for x in str(number)])
        if is_prime(number):
            if len(primes) > 0:
                some_other = random.choice(primes)
            primes.append(number)
            sets.add_with_check(number, data)
            if len(primes) > 1:
                sets.join(number, some_other)
        else:
            if len(non_primes) > 0:
                some_other = random.choice(non_primes)
            non_primes.append(number)
            sets.add_with_check(number, data)
            if len(non_primes) > 1:
                sets.join(number, some_other)
    for i in range(100000):
        a = random.randint(2, 10000)
        res = sets.find_with_check(a)
        if a in primes or a in non_primes:
            assert len(res) == 2
        else:
            assert res is None

def test_disjoint_subsets_with_random_primes_add_by_find():
    primes = []
    non_primes = []
    sets = DisjointSubsets()
    for i in range(1000):
        number = random.randint(2, 10000)
        data = "-".join([x for x in str(number)])
        if is_prime(number):
            if len(primes) > 0:
                some_other = random.choice(primes)
            primes.append(number)
            sets.find_with_add(number, data)
            if len(primes) > 1:
                sets.join(number, some_other)
        else:
            if len(non_primes) > 0:
                some_other = random.choice(non_primes)
            non_primes.append(number)
            sets.find_with_add(number, data)
            if len(non_primes) > 1:
                sets.join(number, some_other)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(non_primes)
        b = random.choice(non_primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(non_primes)
        assert not sets.in_same(a, b)

def test_disjoint_subsets_with_random_primes_join_with_check():
    primes = []
    non_primes = []
    sets = DisjointSubsets()
    for i in range(10000):
        number = random.randint(2, 10000)
        data = "-".join([x for x in str(number)])
        if is_prime(number):
            if len(primes) > 0:
                some_other = random.choice(primes)
            if number in primes:
                if len(primes) > 0:
                    a, b = randomize_order(number, some_other)
                    assert sets.join_with_check(a, b)
            else:
                if len(primes) > 0:
                    a, b = randomize_order(number, some_other)
                    assert not sets.join_with_check(a, b)
                sets.add_with_check(number, data)
                if len(primes) > 0:
                    sets.join(number, some_other)
            primes.append(number)
        else:
            if len(non_primes) > 0:
                some_other = random.choice(non_primes)
            if number in non_primes:
                if len(non_primes) > 0:
                    a, b = randomize_order(number, some_other)
                    assert sets.join_with_check(a, b)
            else:
                if len(non_primes) > 0:
                    a, b = randomize_order(number, some_other)
                    assert not sets.join_with_check(a, b)
                sets.add_with_check(number, data)
                if len(non_primes) > 0:
                    sets.join(number, some_other)
            non_primes.append(number)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(non_primes)
        b = random.choice(non_primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(non_primes)
        assert not sets.in_same(a, b)


def test_disjoint_subsets_with_random_primes_join_with_add():
    primes = []
    non_primes = []
    sets = DisjointSubsets()
    for i in range(10000):
        number = random.randint(2, 10000)
        data = "-".join([x for x in str(number)])
        if is_prime(number):
            if len(primes) > 0:
                some_other = random.choice(primes)
                other_data = "-".join([x for x in str(some_other)])
                sets.join_with_add(number, some_other, data, other_data)
            else:
                sets.add_with_check(number, data)
            primes.append(number)
        else:
            if len(non_primes) > 0:
                some_other = random.choice(non_primes)
                other_data = "-".join([x for x in str(some_other)])
                sets.join_with_add(number, some_other, data, other_data)
            else:
                sets.add_with_check(number, data)
            non_primes.append(number)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(non_primes)
        b = random.choice(non_primes)
        assert sets.in_same(a, b)
    for i in range(1000):
        a = random.choice(primes)
        b = random.choice(non_primes)
        assert not sets.in_same(a, b)

def test_disjoint_subsets_with_random_primes_that_dont_all_exist_in_same_with_check():
    primes = []
    non_primes = []
    sets = DisjointSubsets()
    for i in range(1000):
        number = random.randint(2, 10000)
        data = "-".join([x for x in str(number)])
        if is_prime(number):
            if len(primes) > 0:
                some_other = random.choice(primes)
            primes.append(number)
            sets.add_with_check(number, data)
            if len(primes) > 1:
                sets.join(number, some_other)
        else:
            if len(non_primes) > 0:
                some_other = random.choice(non_primes)
            non_primes.append(number)
            sets.add_with_check(number, data)
            if len(non_primes) > 1:
                sets.join(number, some_other)
    for i in range(100000):
        a = random.randint(2, 10000)
        b = random.randint(2, 10000)
        if a in primes and b in primes or a in non_primes and b in non_primes:
            assert sets.in_same_with_check(a, b)
        else:
            assert not sets.in_same_with_check(a, b)
