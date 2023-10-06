

def p(n, m):
    if n == 0:
        return 1
    return sum([p(i, m) * m**(n - i) for i in range(n)])

def generate(n, m, data, curr):
    if n == 0:
        data.append(curr)
        return
    for i in range(m):
        generate(n - 1, m, data, [x for x in curr] + [i])

def is_pal_hard(arr):
    length = len(arr)
    s = 0
    e = length - 1
    while s < e:
        if arr[s] != arr[e]:
            return False
        s += 1
        e -= 1
    return True

def is_palindrome(arr):
    if arr == []:
        return True
    for i in range(2, len(arr) + 1, 2):
        if is_pal_hard(arr[:i]) and is_palindrome(arr[i:]):
            return True
    return False

def good_formula(n, m):
    if n == 0:
        return 1
    if n == 1:
        return m
    ans = m**n
    for i in range(1, n - 1):
        ans += good_formula(i, m) * m**(n-1) - m
    ans += good_formula(n - 1, m) * (m - 1)
    return ans



def main(n, m):
    formula = p(n // 2, m)
    simpler_formula = m**(n // 2) * 2**(n // 2 - 1)
    combinations = []
    generate(n, m, combinations, [])
    palindromes = [x for x in combinations if is_palindrome(x)]
    guess = good_formula(n // 2, m)
    print(f"n={n}, m={m}, answer: ({formula}, {simpler_formula}, {len(combinations)}, {len(palindromes)}, {guess})")
    print(palindromes)
    print()
    # print(len(palindromes))



if __name__ == '__main__':
    if False:
        a = [int(x) for x in input().split(" ")]
        n, m = a[0], a[1]
        main(n, m)
        exit()
    for n in range(6, 9, 2):
        for m in range(2, 3):
            main(n, m)
