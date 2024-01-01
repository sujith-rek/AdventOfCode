import re

points = 0

with open('input.txt', 'r') as f:
    for line in f:

        card = line.split(':')[1].strip()

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
        
        if poll != 0:
            points += 2 ** (poll-1)
        
print(points)

