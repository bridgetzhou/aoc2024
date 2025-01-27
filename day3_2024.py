'''
'''
import re

# teststring = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

# x = teststring.split("do")  # split the string by delimiter "do"
# # if the new string starts with n't then ignore it, otherwise pull out the mul(#,#)

# print(x)

file = open("/Users/bridgetzhou/Desktop/aoc_2024/day3_input.txt",
            "r", encoding='utf8')
puzzle_input = file.read()

# print(puzzle_input)

# print(re.search('dont', puzzle_input))


def mul(input_data):
    mul_pairs = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input_data)
    mul_pairs2 = []
    for li in mul_pairs:
        li2 = li.replace("mul(", "")
        li3 = li2.replace(")", "")
        li4 = li3.replace(",", " ")
        li5 = [int(ele) for ele in li4.split()]
        mul_pairs2.append(li5)
    f1 = None
    f2 = None
    new_list = []
    for num_pair in mul_pairs2:
        f1 = num_pair[0]
        f2 = num_pair[1]
        new_list.append(f1*f2)
    return sum(new_list)

# part two

#


def mul_2(input_data):
    string_list = input_data.split("do")
    new_list = []
    for string in string_list:
        if string.startswith("n't"):
            new_list.append(0)
        else:
            mul_pairs = re.findall(r"mul\(\d{1,3},\d{1,3}\)", string)
            mul_pairs2 = []
            for li in mul_pairs:
                li2 = li.replace("mul(", "")
                li3 = li2.replace(")", "")
                li4 = li3.replace(",", " ")
                li5 = [int(ele) for ele in li4.split()]
                mul_pairs2.append(li5)
            f1 = None
            f2 = None
            # new_list = []
            for num_pair in mul_pairs2:
                f1 = num_pair[0]
                f2 = num_pair[1]
                new_list.append(f1*f2)
    return sum((new_list))


print(mul_2(puzzle_input))
