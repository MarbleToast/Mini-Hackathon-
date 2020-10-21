def syllable_count(string):
    x=0
    vowels = "aeiouy"
    if (string[0] in vowels):
        x+=1
    for i in range(1, len(string)):
        if (string[i] in vowels and string[i-1] not in vowels):
            x+=1
            if string.endswith("e"):
                x -=1
        if (x == 0):
            x+=1
    return x

print(syllable_count(""))
