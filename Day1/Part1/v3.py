# Initialize the sum
total_sum = 0

# Open the file and process each line
with open('input.txt', 'r') as f:
    for line in f:
        # Initialize an empty string for the current number
        current_number = ''
        # Iterate over each character in the line
        for char in line.strip():
            # If the character is a digit, add it to the current number
            if char.isdigit():
                current_number += char
                break
        
        # iterate over each character in the line in reverse order
        for char in line.strip()[::-1]:
            # If the character is a digit, add it to the current number
            if char.isdigit():
                current_number += char
                break
        

        # If there is a current number at the end of the line, process it
        if current_number:
            total_sum += int(current_number)

# Print the total sum
print(total_sum)