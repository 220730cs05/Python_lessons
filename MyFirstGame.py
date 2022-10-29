# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:40:53 2022

@author: VICTUS
"""

"""(Son topish o'yini)"""

import random
print("Keling, o'ylagan sonni topish o'yinini o'ynaymiz!")
def son_top(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f'Men 1 dan {x} gacha bo\'lgan sonlardan birini o\'yladim. Shu sonni topa olasizmi?')
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input('>>>'))
        if taxmin<tasodifiy_son:
            print('Xato, men o\'ylagan son bundan kattaroq. Yana harakat qilib ko\'ring: ')
        elif taxmin>tasodifiy_son:
            print('Xato, men o\'ylagan son bundan kichikroq. Yana harakat qilib ko\'ring: ')
        else:
            break
    print(f'Tabriklayman, {tasodifiy_son} sonini o\'ylagan edim. {taxminlar} ta taxmin bilan topdingiz!')
    return taxminlar
def son_top_pc(x=10):
    input(f"""
Endi mening navbatim,
1 dan {x} gacha bo\'lgan sonlardan birini o\'ylang, men topaman.
O'ylab bo'lgan bo'lsangiz 'ENTER' tugmasini bosing!""")
    minimum = 1
    maximum = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if minimum != maximum:
            taxmin = random.randint(minimum,maximum)
        else:
            taxmin = minimum
        javob = input(f"""Siz {taxmin} sonini o'yladingiz: Agarda to'g'ri bo'lsa (t) ni bosing,
"""
        f"""o'ylagan soningiz bundan kattaroq bo'lsa (+) ni, kichikroq bo'lsa (-) ni bosing. """).lower()
        if javob == "-":
            maximum = taxmin - 1
        elif javob == "+":
            minimum = taxmin + 1
        else:
            break
    print(f"Soningizni {taxminlar} ta taxmin bilan topdim!")
    return taxminlar
    
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = son_top_pc(x)
        if taxminlar_user>taxminlar_pc:
            print(f"""
Men {taxminlar_pc} ta taxmin bilan topdim va yutdim!""")
        elif taxminlar_user<taxminlar_pc:
            print(f"""
Siz {taxminlar_user} ta taxmin bilan topdingiz va yutdingiz!""")
        else:
            print("""
Durrang!""")
        yana = int(input('Yana o\'ynaysizmi? O\'ynasangiz (1) ni, o\'ynamasangiz (0) ni kiriting: '))
print(play())

    
    