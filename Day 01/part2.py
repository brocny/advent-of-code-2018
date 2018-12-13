sm = 0
st = set()

while(1):
    for x in open('input.txt').read().splitlines():
        sm += int(x)
        if sm in st:
            print(sm)
            exit()
        st.add(sm)