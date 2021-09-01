# Reverse Complement :
# A DNA string is made up of four symbols: A, T, C, and G. Each symbol has a complement:
# A and T complement each other
# C and G complement each other

# We define the reverse complement of a DNA string to be the string formed by reversing the symbols in the string and taking 
# the complement of each symbol. For example, to find the reverse complement of s = GTCAG, we first reverse GTCAG -> GACTG then we 
# complement each symbol to get CTGAC.
# Your task is to print the reverse complement of the input string.


# Input Format : The only line of input consists of the string s.


# Constraints
# 1 <= |s| <= 1000
# Each character s[i] = {A,T,C,G}


# Output Format: Print the reverse complement of the given string.


# Sample TestCase 1
# Input
# ATGC
# Output
# GCAT
# Explanation
# When we reverse s = ATGC, we get CGTA. We then return the complement of the reversed string, which is sc = GCAT.

# Sample TestCase 2
# Input
# ACCGGGTTTT
# Output
# AAAACCCGGT
# Explanation
# When we reverse s = ACCGGGTTTT, we get TTTTGGGCCA. We then return the complement of the reversed string, which is sc = AAAACCCGGT.

# Sample TestCase 3
# Input
# ATCGTA
# Output
# TACGAT
# Explanation
# When we reverse s = ATCGTA, we get ATGCTA. We then return the complement of the reversed string, which is sc = TACGAT.



s = input()
txt = s[::-1]
com =''
for i in txt:
    if i == 'A' :
        com = com + 'T'
    elif i == 'T' :
        com = com + 'A'
    elif i == 'G':
        com = com + 'C'
    elif i == 'C' :
        com = com + 'G'

print(com)