import random
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0


def start():
    print("Let's play game of Rock, Paper, Scissors.\n")
    while game():
        pass
    scores()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print("Rock = 1 \nPaper = 2\nScissors = 3 \nMake a move: ")
        try:
            player = int(input())
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Input is Invalid.\nPlease enter 1, 2 or 3 only.")


def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(2)
    print("3!")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer]))

    global player_score, computer_score
    if player == computer:
        print("Tie Game.")
    else:
        if rules[player] == computer:
            print("Your victory is assured.")
            player_score += 1
        else:
            print("The computer laughs as you realise you have been defeated.")
            computer_score += 1


def play_again():
    answer = input("Would you like to play again? Y/N: ")
    if answer in ("y", "Y", "yes", "Yes"):
        return answer

    else:
        print("Thank you very much for playing our game. See you next time!")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


if __name__ == '__main__':
    start()
