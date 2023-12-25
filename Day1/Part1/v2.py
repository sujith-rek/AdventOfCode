import re

# Initialize the sum
total_sum = 0

# Open the file and process each line
with open('input.txt', 'r') as f:
    for line in f:
        # Find all the numbers in the line
        numbers = re.findall(r'\d+', line.strip())
        # Join the numbers into a single string
        number_str = ''.join(numbers)
        # Add the first and last digits of the number to the total sum
        if number_str:
            total_sum += int(number_str[0]+number_str[-1])

# Print the total sum
print(total_sum)
