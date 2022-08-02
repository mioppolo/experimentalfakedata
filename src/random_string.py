'''
Generate a list of random strings. The length of the string is determined by a chi square distribution and a ceiling function.
'''

import string
import random
import math
from scipy.stats import chi2

alphabet = string.ascii_lowercase + string.ascii_uppercase

def random_string(symbols, length):
    return ''.join(random.choices(symbols,k=length))

def random_strings(symbols, number): 
    lengths = [math.ceil(i) for i in chi2.rvs(df=9, size = number)]
    strings = [random_string(symbols, n) for n in lengths]
    return strings

if __name__ == '__main__':
    #print(''.join(random.choices(string.ascii_lowercase,k=10)))
    #print(random_string(alphabet,12)
    print(random_strings(alphabet, 10))
