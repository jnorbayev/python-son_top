"""
18.05.2022 15:43

"SON TOPISH" o'yini

Muallif : Javlonbek Norbayev
O'qituvchi : Anvar Nazrullayev

GitHub sahifa :  https://github.com/jnorbayev
"""

import random


def sontop(x=10):
    """Kopmyuter son o'ylaydi, inson esa uni topishi kerak """
    t_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi ?")
    taxminlar = 0

    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < t_son:
            print("Xato. Men bundan kattaroq son o'ylagandim. Qaytadan kiriting: ")
        elif taxmin > t_son:
            print("Xato. Men bundan kichikroq son o'ylagandim. Qaytadan kiriting: ")
        else:
            break
    print(f"Tabriklaymiz. {taxminlar}ta taxmin bilan topdingiz !!!")
    return taxminlar


def sontop_pc(x=10):
    """Inson son o'ylaydi pc topishi kerak"""
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t), "
                      f"men o'ylagan son bundan kattaroq(+), kichikroq(-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim !!!")
    return taxminlar


def play(x=10):
    yana = True
    while yana:
        taxminlar_human = sontop(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_human > taxminlar_pc:
            print("Men yutdim !")
        elif taxminlar_human < taxminlar_pc:
            print("Siz yutdingiz !")
        else:
            print("Durrang !")
        yana = int(input("Yana o'ynaysizmi? Ha(1) / Yo'q(0):"))


play()
