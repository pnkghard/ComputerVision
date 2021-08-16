import numpy as np


def chekMatch(name_1, name_2, i, n):
    if i==n:
        return True
    if name_1[i] != name_2[i]:
        return False
    chekMatch(name_1, name_2, i+1, n)

# Arranging the word
def arangeWord(nam_1, nam_2, i, n):

    if i==n:
        print("MATCH")
        return

    name_1 = nam_1[i]
    name_2 = nam_2[i]

    k=0
    if len(name_1)>len(name_2):
        k = len(name_2)
    else:
        k = len(name_1)
    

    if chekMatch(name_1, name_2, 0, k) == False:
        print("NOT MATCH")
        return
    
    arangeWord(nam_1, nam_2, i+1, n)
    


# Match Customer with comman name
nam_1 = input()
nam_2 = input()

# remove Mr., Mrs, Ms., Shri. from name of the customers
name = nam_1.replace('Mr. ', "")
name = name.replace('Mrs. ', "")
name = name.replace('Ms. ', "")
nam_1 = name.replace('Shri. ', "")

name = nam_2.replace('Mr. ', "")
name = name.replace('Mrs. ', "")
name = name.replace('Ms. ', "")
nam_2 = name.replace('Shri. ', "")

#Splite String in part
nam_1 = nam_1.split(" ")
nam_1=np.char.upper(nam_1)

nam_2 = nam_2.split(" ")
nam_2 = np.char.upper(nam_2)



nam_1.sort()
nam_2.sort()



n = 0
if len(nam_1)>len(nam_2):
    n = len(nam_2)
else :
    n = len(nam_1)

arangeWord(nam_1, nam_2, 0, n)