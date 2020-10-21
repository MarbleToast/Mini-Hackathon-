# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:09:03 2020

@author: jrbra
"""
import pyphen
dic = pyphen.Pyphen(lang='en')


def read_word_list():
    with open("word_list.txt", "r") as f  :
        return [i.strip() for i in f.readlines()]
    
    
def syllable_count(word):
    return len(dic.inserted(word).split("-"))


def parse_syllables():
    syl_dict = {}
    for word in read_word_list():
        syl_count = syllable_count(word)
        if not syl_count in syl_dict.keys():
            syl_dict[syl_count] = [word]
        else:
            syl_dict[syl_count].append(word)
    return syl_dict


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        subset_sum(numbers, target, partial + [n])

syl_dictionary = parse_syllables()
print(subset_sum(list(syl_dictionary.keys()), 2))