# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 22:19:09 2022

@author: VICTUS
"""

import random
from enwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    # letter of the word
    word_letters = set(word)
    # Entered letters from the user
    user_letters = ''
    print(f"""
Men {len(word)} ta harfdan iborat Inglizcha so'z o'yladim. Topa olasizmi?""") 
    # print(word)
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritgan hraflaringiz: {user_letters}")
        
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting: ")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri.")
        else:
            print("Bunday harf yo'q")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinish bilan topdingiz.")
    