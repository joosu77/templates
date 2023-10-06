

def main():
    t = int(input())
    for _ in range(t):
        inp = input().split(" ")
        n = int(inp[0])
        slices = set()
        for j in inp[1:]:
            a = int(j)
            a = a % 360
            if a >= 180:
                a = a - 180
            slices.add(a)
        length = len(slices)
        if length == 0:
            print(1)
        else:
            print(length * 2)


if __name__ == '__main__':
    main()
