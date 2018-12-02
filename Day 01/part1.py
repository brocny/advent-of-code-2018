def main():
    sum = 0
    with open('input.txt') as  f:
        for x in f:
            num = int(x[1:])
            sum += num if x[0] == '+' else -num

    print(sum)

if __name__ == "__main__":
    main()


