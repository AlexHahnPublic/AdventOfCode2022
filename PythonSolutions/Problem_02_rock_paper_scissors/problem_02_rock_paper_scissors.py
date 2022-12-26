##########################################################################
##########################################################################
#
# File Name:
#            problem_02_rock_paper_scissors.py
#
# Descrption:
#            Problem 2 of the 2022 Advent of code, solved in python
# Author:
#            Alex Hahn
#
##########################################################################
##########################################################################


# There are only 9 possible in the cartesion product of two length three vectors
# We will define a dict where the keys are the two tuples of the 9 combinations and the value is the score

scores1 = {
("A","X"): 4, # Tie (3)  + Rock (1)     = 4
("A","Y"): 8, # Win (6)  + Paper (2)    = 8
("A","Z"): 3, # Loss (0) + Scissors (3) = 3
("B","X"): 1, # Loss (0) + Rock (1)     = 1
("B","Y"): 5, # Tie (3)  + Paper (2)    = 5
("B","Z"): 9, # Win (6)  + Scissors (3) = 9
("C","X"): 7, # Win (6)  + Rock (1)     = 7
("C","Y"): 2, # Loss (0) + Paper (2)    = 2
("C","Z"): 6, # Tie (3)  + Scissors (3) = 6
}

scores2 = {
("A","X"): 3, # Lose (0) + Scissor (3)  = 3
("A","Y"): 4, # Tie (3)  + Rock (1)     = 4
("A","Z"): 8, # Win (6)  + Paper (2)    = 8
("B","X"): 1, # Loss (0) + Rock (1)     = 1
("B","Y"): 5, # Tie (3)  + Paper (2)    = 5
("B","Z"): 9, # Win (6)  + Scissors (3) = 9
("C","X"): 2, # Loss (0) + Paper (2)    = 2
("C","Y"): 6, # Tie (3)  + Scissors (3) = 6
("C","Z"): 7, # Win (6)  + Rock (1)     = 7
}

total1 = 0
total2 = 0

with open('strategy.txt') as f:
    for row in f:
        total1 = total1 + scores1[(row[0],row[2])]
        total2 = total2 + scores2[(row[0],row[2])]


print("First Total score is: " + str(total1))
print("Second Total Sore is: " + str(total2))
