import random

def play (computer):
    user = input("whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    if user == computer:
        return 0

    if user == 'p' and computer == 'r':
        return 1
    if user == 'p' and computer == 's':
        return 2
    if user == 'r' and computer == 's':
        return 2
    if user == 'r' and computer == 'p':
        return 1
    if user == 's' and computer == 'r':
        return 2
    if user == 's' and computer == 'p':
        return 1

    print("that is not aloud please put r, s or p")

max_score=5
player_score=0
computer_score=0
while (player_score < max_score and computer_score < max_score):
    computer = random.choice('r' 'p' 's')
    result = play(computer)
    if result == 0:
        print("you and the computer have both chosen {} it is a tie".format(computer))
    elif result == 1:
        print("you won computer picked {}".format(computer))
        player_score+=1
    elif result == 2:
        print("you lose computer picked {}".format(computer))
        computer_score+=1

if player_score > computer_score:
    print("player won the game with {} against {}".format(player_score,computer_score))
else:
    print("computer won the game with {} against {}".format(computer_score,player_score))

