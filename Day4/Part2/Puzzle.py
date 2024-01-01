import re

points = 0

# num = [1 for i in range(6)]
num = [1 for i in range(216)]

with open('input.txt', 'r') as f:
    for line in f:
        no,card = line.split(':')
        no = no.split(' ')[-1].strip()
        no = int(no)

        winning_cards, current_card = card.split('|')

        winning_numbers = []
        poll = 0
        # spilt the winning cards by ' ' and store the numbers in a list
        for winning_card in winning_cards.split(' '):
            if winning_card == '':
                continue
            winning_numbers.append(int(winning_card))
        
        for current_card in current_card.split(' '):
            if current_card == '':
                continue
            current_card = int(current_card)
            if current_card in winning_numbers:
                poll += 1
        print(no,poll)
        
        for i in range(no,no+poll):
            num[i] += num[no-1]
        
print(sum(num))

