# Curious Shubham :
# There are 26 groups of people in Shubham's Company. At lunchtime, they all want to get some food to eat as soon as possible. All the groups have made plan to get some food as soon as possible. According to the plan, every person of the group will share the description of food he/she wants to eat so that all the group members will be able to order the food on the behalf of his/her group. All the persons stand at various locations in the queue and whoever will get the food first, will distribute the food among all the group.

# But there is a weird procedure of getting the food from a queue. People having even indices form a new queue and process repeats until only 1 person remains in the queue. He/she will be able to order some food of his choice. Shubham and his friends are curious about the group which will be able to get some food.

# Input Format:
#             The first line of input consists of the number of people present in the Queue, N.
#             The second line of input consists of a string that represents the group of each person who is standing in the queue.


# Constraints:    1<= N <=25000000

# The string consists of uppercase letters only.


# Output Format:  Print a single character which represents the group of the person who will be able to get the food first.

# Sample TestCase 1:
# Input:  10
#         GKFXGHMSHQ

# Output: S

def getFood(s, n):
    if len(s) == 1:
        print(s)
        return
    new = ""
    for i in range(1, n, 2):
        new = new + s[i]
    getFood(new, (int)(n/2))
    

def main():

    n = int(input())

    s = input()

    getFood(s, n)

main()