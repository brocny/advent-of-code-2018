def main():
    appeared_twice = 0
    appeared_thrice = 0
    with open('input.txt') as f:
        for line in f:
            d = {}
            for char in line:
                d[char] = d.get(char, 0) + 1
            if any(filter(lambda x: d[x] == 3, d)):
                appeared_thrice += 1
            if any(filter(lambda x: d[x] == 2, d)):
                appeared_twice += 1
    print(appeared_thrice * appeared_twice)
             


if __name__ == "__main__":
    main()