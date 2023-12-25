dictonary = {
    'eight': '8',
    'five': '5',
    'four': '4',
    'nine': '9',
    'one': '1',
    'seven': '7',
    'six': '6',
    'three': '3',
    'two': '2',
}

start_arr = ['e', 'f', 'n', 'o', 's', 't']
check_dict = {
    'e': 5,
    'f': 4,
    'n': 4,
    'o': 3,
    's': 5,
    't': 5,
}

# sample input
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen


total_sum = 0

with open('input.txt', 'r') as f:
    for line in f:
        
        # for each character in the line
        # check if it is in the start_arr
        # if yes, check if the next check_dict[char] characters and see if they are in the dictonary
        # if yes, replace the word with the number
        # if no, skip those many characters

        iter_string = ''
        new_line = ''
        i = 0
        while i < len(line.strip()):
            if i <= len(line.strip())-1 and line[i] in start_arr:
                iter_string = line[i:i+check_dict[line[i]]]
                if iter_string in dictonary:
                    new_line += dictonary[iter_string]
                    i += check_dict[line[i]]-1
                elif line[i]=='t' and line[i+1]=='w' and line[i+2]=='o':
                    new_line += '2'
                    i += 2
                elif line[i]=='s' and line[i+1]=='i' and line[i+2]=='x':
                    new_line += '6'
                    i += 2
                else:
                    i += 1
            else:
                if line[i].isdigit():
                    new_line += line[i]
                i += 1
            
        number_str = new_line.strip()
        if number_str:
            make_number = int(number_str[0]+number_str[-1])
            total_sum += make_number
        print(number_str, make_number,end=' \n')

print(total_sum)
