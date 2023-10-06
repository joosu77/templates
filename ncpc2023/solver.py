#!/home/krissu/anaconda3/bin/python3


def main():
    amount = int(input())
    total = 0
    for i in range(amount):
        total += int(input())
        print(total)


main()
