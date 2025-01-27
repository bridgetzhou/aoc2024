# load the txt file
# unpack into the two lists
# convert to python list type and sort smallest to largest
# calculate difference between the values with matching indices
# and place those differences in a new list
# sum up the list of differences

# examplelists
import numpy as np
l1 = sorted([3, 4, 2, 1, 3, 3])
l2 = sorted([4, 3, 5, 3, 9, 3])
# part 1


list1, list2 = np.loadtxt(
    "/Users/bridgetzhou/Desktop/aoc_2024/day1_input.txt", unpack=True)
list1 = sorted(list(list1))
list2 = sorted(list(list2))


diffs = []

for i, value in enumerate(list1):
    diffs.append(abs(list1[i]-list2[i]))
print(sum(diffs))

# part two
common_values = list(set(list1).intersection(set(list2)))

reps = []
for a in common_values:
    reps.append(list2.count(a))
s_score = []
for i, value in enumerate(common_values):
    s_score.append(common_values[i]*reps[i])

print(sum(s_score))
