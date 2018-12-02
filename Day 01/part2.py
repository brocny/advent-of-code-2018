def main():
    sum = 0
    st = set()

    while(True):
        with open('input.txt') as f:
            for x in f:
                num = int(x[1:])
                sum += num if x[0] == '+' else -num
                if sum in st:
                    print(sum)
                    return
                st.add(sum)

if __name__ == "__main__":
    main()


