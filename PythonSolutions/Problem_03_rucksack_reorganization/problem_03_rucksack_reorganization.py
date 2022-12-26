##########################################################################
##########################################################################
#
# File Name:
#            problem_03_rucksack_reorganization.py
#
# Descrption:
#            Problem 3 of the 2022 Advent of code, solved in python
# Author:
#            Alex Hahn
#
##########################################################################
##########################################################################



# small helper to convert character to its "priority" value as specified in the problem statement
def priority(c):
    if(c.isupper()):
        return(ord(c) - 38)
    else:
        return(ord(c) - 96)

total = 0
with open("rucksacks.txt", "r") as rucksacks:
    for sack in rucksacks:

        # compute the indices to break the compartments into
        n = len(sack)
        h = n/2

        # create the two lists (compartments)
        l1 = sack[0:h]
        l2 = sack[h:n]

        # calc intersection (note must be a set, can write with list comprehension seen/ not seen fashion)
        total = total + priority(list(set(l1).intersection(l2))[0])

    print(total)
