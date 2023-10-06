
mods = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0)
}

def gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = gcd(b, a % b)
    return d, y1, x1 - y1 * (a // b)

def find_any_solution(a, b, c):
    g, x0, y0 = gcd(abs(a), abs(b))
    if c % g:
        return False, None, None, None
    x0 *= (c // g)
    y0 *= (c // g)
    if a < 0:
        x0 = - x0
    if b < 0:
        y0 = - y0
    return True, x0, y0, g

def main():
    t = int(input())
    for _ in range(t):
        r = int(input())
        room = []
        for i in range(r):
            room.append(input().strip("\n"))
        ld = int(input())
        d = {}
        dlist = []
        for i in range(ld):
            inp = [int(x) for x in input().split(" ")]
            d[(inp[0], inp[1])] = i
            dlist.append((inp[0], inp[1]))
        rx = 0
        ry = 0
        r = {}
        rlist = []
        c = 0
        impossible = False
        while len(rlist) == 0 or rx != 0 or ry != 0:
            if (rx, ry) in r.keys():
                impossible = True
                break
            r[(rx, ry)] = len(rlist)
            rlist.append((rx, ry))
            dx, dy = mods[room[ry][rx]]
            rx += dx
            ry += dy
        if impossible:
            print("never")
            continue
        lr = len(rlist)
        common = []
        if len(rlist) < len(dlist):
            for x, y in rlist:
                if (x, y) in d.keys():
                    common.append((x, y))
        else:
            for x, y in dlist:
                if (x, y) in r.keys():
                    common.append((x, y))
        earliest = -1
        for x, y in common:
            rp = r[(x, y)]
            dp = d[(x, y)]
            c = rp - dp
            has_solutions, x0, y0, g = find_any_solution(ld, -lr, c)
            if not has_solutions:
                continue
            k = 0
            bg = - lr // g
            ag = - ld // g
            xa = x0
            ya = y0
            print(rp + y * lr, dp + x * ld)
            while xa > 0 or ya > 0:
                xa += bg
                ya += ag
            while xa < 0 or ya < 0:
                xa -= bg
                ya -= ag
            print(rp + y * lr, dp + x * ld)
            print()
            # print(x, y, xa, ya, g)
            # print(c)
        if impossible:
            print("never")
            continue
        print()
        print(len(rlist), len(dlist))
        print(common)
        print()
        print()





if __name__ == '__main__':
    main()
