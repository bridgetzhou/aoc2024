with open('/Users/bridgetzhou/Desktop/aoc_2024/day4_input.txt', 'r', encoding='UTF-8') as my_file:
    my_file2 = my_file.read()

puzzle_input = my_file2.split('\n')

# now x is a list of strings
xmas_count = []
for row in puzzle_input:  # for each row of the word search
    for i, item in row:  # for each letter in a row
        if item == 'x':  # if the letter is an x
            if item[i+1] == 'M' and item[i+2] == 'A' and item[i+3] == 'S':
                xmas_count.append(1)
        else:
            continue  # if it not an x, check the next letter
