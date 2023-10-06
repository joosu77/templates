import math

q = int(input())

def get_dir(inst):
    if inst == ">":
        return (0, 1)
    if inst == "<":
        return (0, -1)
    if inst == "v":
        return (1, 0)
    if inst == "^":
        return (-1, 0)

def get_robot_path(map, start=(0, 0)):
    current = start
    time = 0
    path = {0: current, current: 0}
    loc = (-1, -1)
    while loc == (-1, -1) or tuple(current[i] + get_dir(map[current[0]][current[1]])[i] for i in range(2)) not in path:
        action = map[current[0]][current[1]]
        loc = tuple(current[i] + get_dir(action)[i] for i in range(2))
        time += 1
        path[loc] = time
        path[time] = loc
        current = loc
    if start == tuple(current[i] + get_dir(map[current[0]][current[1]])[i] for i in range(2)):
        return path, None, None
    start = tuple(current[i] + get_dir(map[current[0]][current[1]])[i] for i in range(2))
    cycle_path, _, _ = get_robot_path(map, start=start)
    time = max(x for x in cycle_path.keys() if type(x) == int) + 1

    for i in cycle_path.keys():
        del path[i]
    return cycle_path, path, time


def gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = gcd(b, a % b)
    return d, y1, x1 - y1 * (a // b)


for _ in range(q):
    r = int(input())
    map = []
    for _ in range(r):
        map.append(list(input().strip()))
    cycle_path, start_path, cycle_len = get_robot_path(map)
    if start_path == None:
        time_to_get_to_cycle = 0
        cycle_len = max(x for x in cycle_path.values() if type(x) == int) + 1
    else:
        time_to_get_to_cycle = max(x for x in start_path.values() if type(x) == int) + 1
    d = int(input())
    min_val = math.inf
    # b_set = set()
    # btime = time_to_get_to_cycle + cycle_path[()]
    # for b in range(200)
    for time in range(d):
        # not in cycle
        y, x = [int(a) for a in input().split(" ")]
        if start_path is not None and (y, x) in start_path:
            if time == start_path[(y, x)]:
                min_val = min(time, min_val)
                continue

        # not in cycle
        if (y, x) not in cycle_path:
            continue

        leaf_times = set()
        atime = time
        for a in range(35):
            leaf_times.add(atime)
            atime += d

        btime = time_to_get_to_cycle + cycle_path[(y, x)]
        for b in range(35):
            if btime in leaf_times:
                min_val = min(btime, min_val)
            btime += cycle_len


    if min_val == math.inf:
        print("never")
        continue
    print(min_val)






"""
1
3
v>v
>^<
^^^
2
2 0
1 1
"""
