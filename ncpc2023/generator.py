import random


lowercase = "qwertyuiopasdfghjklzxcvbnm"
uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
alpha = lowercase + uppercase
numeric = "0123456789"
alphanumeric = alpha + numeric
hex_lower = "0123456789abcdef"
hex_upper = "0123456789ABCDEF"


def random_string(alphabet, length):
    return "".join([random.choice(alphabet) for _ in range(length)])


def datapoint_generator():
    return random.randint(100, 1000)


def linedata_generator():
    return [datapoint_generator() for _ in range(1)]


def generator_single():
    n = random.randint(2, 100)
    others = []
    for i in range(n):
        linedata = linedata_generator()
        others.append(linedata)
    return [[n]] + others


def generator_multi():
    n = random.randint(5, 10)
    data = []
    data.append([n])
    for _ in range(n):
        data += generator_single()
    return data


def to_line(x):
    return " ".join([str(a) for a in x])


def line_generator():
    data = generator_multi()
    return [to_line(x) for x in data]


def main():
    filename = "random.txt"
    lines = line_generator()
    file = open(f"input/{filename}", "w")
    file.write("\n".join(lines))
    file.close()


if __name__ == '__main__':
    main()
