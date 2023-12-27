# Game 33: 12 red, 4 green, 11 blue; 4 blue, 10 red, 1 green; 7 green, 10 red, 16 blue; 15 red, 5 blue; 10 green, 4 red; 8 green, 5 blue, 6 red
import re

power = 0

with open('input.txt', 'r') as f:
    for line in f:

        # each trail of a game is separated by a semicolon
        trials = line.split(':')[1].split(';')
        num_trials = len(trials)

        red = 1
        green = 1
        blue = 1

        for trial in trials:

            colors = trial.split(',')
            num_colors = len(colors)

            for color in colors:
                color = color.strip()
                ball_details = color.split(' ')
                # if int(ball_details[0]) > balls[ball_details[1]]:
                #     flag = True
                #     break
                if ball_details[1] == 'red':
                    red = max(red, int(ball_details[0]))
                elif ball_details[1] == 'green':
                    green = max(green, int(ball_details[0]))
                else:
                    blue = max(blue, int(ball_details[0]))
        power += red * green * blue


print(power)

        