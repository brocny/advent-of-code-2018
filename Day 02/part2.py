def main():
    with open('input.txt') as f:
        lst = [line for line in f]

    ln = len(lst)
    func = lambda a: a[0] == a[1]
    for i in range(ln):
        for j in range(i + 1, ln):
            diff_chars = 0
            for x, y in zip(lst[i], lst[j]):
                diff_chars += x != y
            if diff_chars == 1:
                answer = map(lambda x: x[0], filter(func, zip(lst[i][:-1], lst[j][:-1])))
                print("".join(answer))
                return
            
             


if __name__ == "__main__":
    main()