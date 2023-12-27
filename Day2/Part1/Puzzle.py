# Game 33: 12 red, 4 green, 11 blue; 4 blue, 10 red, 1 green; 7 green, 10 red, 16 blue; 15 red, 5 blue; 10 green, 4 red; 8 green, 5 blue, 6 red
import re

balls = {
    'red': 12,
    'green': 13,
    'blue': 14
}

wrong_ids = 0

with open('input.txt', 'r') as f:
    for line in f:
        game_id = re.search(r'Game (\d+):', line)
        game_id = int(game_id.group(1))

        # each trail of a game is separated by a semicolon
        trials = line.split(':')[1].split(';')
        num_trials = len(trials)
        flag = False

        for trial in trials:
            if flag:
                break

            colors = trial.split(',')
            num_colors = len(colors)

            for color in colors:
                color = color.strip()
                ball_details = color.split(' ')
                if int(ball_details[0]) > balls[ball_details[1]]:
                    flag = True
                    break
        if not flag:
            wrong_ids += game_id 


print(wrong_ids)

        