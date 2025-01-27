# day 2 of AoC 2024 part two

def conv_func(string):
    res = [int(ele) for ele in string.split(' ')]
    return list(res)


with open("/Users/bridgetzhou/Desktop/aoc_2024/day2_input.txt", 'r', encoding='utf8') as file:
    numbers = file.readlines()

puzzle_input = []

for num in numbers:
    a = num.rstrip('\n')
    puzzle_input.append(conv_func(a))


# def make_sublist(y):
#     sublist = []
#     for i in range(len(y)):  # make sublists of the list
#         sublist = [r for id, r in enumerate(y) if id != i]
#         print(sublist)


# make_sublist([1, 3, 2, 4, 5])


def problem_dampener(x):
    sublist = []
    sd_li = []
    status = None
    for i in range(len(x)):  # make sublists of the list
        sublist = [r for id, r in enumerate(x) if id != i]
        sd_li = [sublist[j+1] - sublist[j] for j in range(len(sublist)-1)]
        if all(val > 0 for val in sd_li) and all(0 < val <= 3 for val in sd_li):
            status = True
            break
        elif all(v < 0 for v in sd_li) and all(-3 <= val <= -1 for val in sd_li):
            status = True
            break
        else:
            status = False
    return status


def is_safe(puzz_input):
    safety_status = []
    for li in puzz_input:
        diff_list = [li[i+1] - li[i] for i in range(len(li)-1)]
        if all(val > 0 for val in diff_list) and all(0 < val <= 3 for val in diff_list):
            safety_status.append('Safe')
        elif all(val < 0 for val in diff_list) and all(0 < abs(val) <= 3 for val in diff_list):
            safety_status.append('Safe')
        else:
            safety_status.append('Unsafe')
    return safety_status


def is_safe2(puzz_input):
    safety_status = []
    for li in puzz_input:
        diff_list = [li[i+1] - li[i] for i in range(len(li)-1)]
        if all(val > 0 for val in diff_list) and all(0 < val <= 3 for val in diff_list):
            safety_status.append('Safe')
        elif all(val < 0 for val in diff_list) and all(0 < abs(val) <= 3 for val in diff_list):
            safety_status.append('Safe')
        elif problem_dampener(li):
            safety_status.append('Safe')
        else:
            safety_status.append('Unsafe')
    return safety_status


print(is_safe2(puzzle_input).count('Safe'))
