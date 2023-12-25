import re

# take input.txt as input and save it as a list
li = []
with open('input.txt', 'r') as f:
    for line in f:
        li.append(line.strip())

# in each line remove all the characters except the numbers
new_regex = re.compile(r'\d+')
li = [new_regex.findall(i) for i in li]

# in each line convert the element into single string
li = [''.join(i) for i in li]

# in each line convert the element into string of li.charAt(0)+li.charAt(-1) converted into integer and sum them up
print(sum([int(i[0]+i[-1]) for i in li]))

