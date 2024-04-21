a - [
    "ehad eloheno eloheno shebashamayim uva'aretz",
    "placeholder2",
    "placeholder3",
    "placeholder4",
    "placeholder5",
    "placeholder6",
    "yemei shabta",
    "yemei mila",
    "yarchei leda",
    "placeholder10",
    "kohvaya",
    "placeholder12",
    "midaya",
]


def b(e):
    def c(num):
        print(num, a[num - 1])
        if num > 1:
            c(num - 1)
    print(e, "mi yodea?")
    print(e, "ani yodea!")
    c(e)
    print()


def d():
    for i in range(1, 14):
        b(i)


d()
