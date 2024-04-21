ani_yodea = [
    "ehad eloheno eloheno shebashamayim uva'aretz",
    'luhot habrit',
    'avot',
    'imahot',
    'chumshei tora',
    'sidrei mishna',
    "yemei shabta",
    "yemei mila",
    "yarchei leda",
    "dibraya",
    "kohvaya",
    "shivtaya",
    "midaya",
]


def mi_yodea(num):
    print(num, ani_yodea[num - 1])
    if num > 1:
        mi_yodea(num - 1)


def verse(num):
    print(num, "mi yodea?")
    print(num, "ani yodea!")
    mi_yodea(num)
    print()


def sing():
    for i in range(1, 14):
        verse(i)


sing()
