a - [
    "placeholder1",
    "placeholder2",
    "placeholder3",
    "placeholder4",
    "placeholder5",
    "placeholder6",
    "yemei shabta",
    "placeholder8",
    "placeholder9",
    "placeholder10",
    "placeholder11",
    "placeholder12",
    "placeholder13",
]


def b(e):
    def c(f):
        print(f, a[f - 1])
        if f > 1:
            c(f - 1)
    print(e, "mi yodea?")
    print(e, "ani yodea!")
    c(e)
    print()


def d():
    for i in range(1, 14):
        b(i)


d()
