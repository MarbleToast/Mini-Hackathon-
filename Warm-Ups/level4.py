""" Hackathon - Level 4 """
def double_swap(x, a, b):
    x = x.replace(a,'$') #I'll assume that there won't be any dollar signs in the string.
    x = x.replace(b,a)
    x = x.replace('$',b)




    return x


if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return ienv, ivdv, ivcv
    print(double_swap('veni, vidi, vici', 'v', 'i'))
