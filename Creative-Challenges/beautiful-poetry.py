# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:09:03 2020

@author: jrbra
"""
import re

def read_word_list():
    with open("word_list.txt", "r") as f  :
        return [i.strip() for i in f.readlines()]
    
def syllable_count(word):
    regex = r"([^aeiouy])(a|e|i|o|u|y)"
    
    matches = re.findall(regex, word, re.MULTILINE)
    
    count = len(matches)
    if ['a', 'e', 'i', 'o', 'u'].__contains__(word[0]):
        count+=1
    return count

print(syllable_count("What"))