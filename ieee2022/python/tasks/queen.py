
q = int(input())
for _ in range(q):
    k, a, b = [int(x) for x in input().split(" ")]
    if a < b:
        a, b, = b, a
    print(a, b)
    if b * (k + 2) == a:
        print("0")
    else:
        print("1")
