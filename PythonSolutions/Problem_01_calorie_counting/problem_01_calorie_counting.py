##########################################################################
##########################################################################
#
# File Name:
#            problem_01_calorie_counting.py
#
# Descrption:
#            Problem 1 of the 2022 Advent of code, solved in python
# Author:
#            Alex Hahn
#
##########################################################################
##########################################################################

calories_file = open("calories.txt", "r")
calories_data = calories_file.read()

calories_all  = calories_data.split("\n")

# loop throw elements and either keep running sum or create a new list with sum 0
total_cals = [0]
for c in calories_all:
    if c == "":
        total_cals.append(0) # a new elf starting with zero cals as we process their list
    else:
        total_cals[len(total_cals)-1] = total_cals[len(total_cals)-1] + int(c) # same elf, update their running sum of total calories

print("Part 1: The elf with the most calories has " + str(max(total_cals)) + " calories\n")

total_cals.sort(reverse=True)
top_three_cals_total = sum(total_cals[0:3])
print("Part 2: The sum of the top three calorie carrying elves is: " + str(top_three_cals_total) + "\n")
