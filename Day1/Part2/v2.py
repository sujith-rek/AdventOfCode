dictionary = {
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

start_arr = {'e', 'f', 'n', 'o', 's', 't'}

check_dict = {
    'e': 5,
    'f': 4,
    'n': 4,
    'o': 3,
    's': 5,
    't': 5,
}

def convert_word(word):
    if word in dictionary:
        return dictionary[word]
    elif word == 'two':
        return '2'
    elif word == 'six':
        return '6'
    else:
        return ''

def process_line(line):
    total_sum = 0
    i = 0
    while i < len(line):
        if line[i] in start_arr:
            word_length = check_dict[line[i]]
            word = line[i:i+word_length]
            replacement = convert_word(word)
            if replacement:
                line = line[:i] + replacement + line[i+word_length:]
                total_sum += int(replacement[0] + replacement[-1])
        i += 1
    return line.strip(), total_sum

total_sum = 0

with open('input.txt', 'r') as f:
    for line in f:
        number_str, make_number = process_line(line)
        if number_str:
            total_sum += make_number
        print(number_str, make_number)

print(total_sum)
