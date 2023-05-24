import random

#inserindo as bases 
print("Let's start a play, rock, paper and scissors!")
user = input("What's your choise: rock, paper or scissors: ")
computer = random.choice(["rock", "paper", "scissors"])

#função que chama a partida
def play(player1, player2):
    print("I chose: ", player2)
    if player1 == player2:
        return print("It's a tie!")
    who_win(player1, player2)

#função que define quem venceu
def who_win(p, c):
    if (p == "rock" and c == "scissors") or (p == "scissors" and c == "paper") \
        or (p =="paper" and c == "rock"):
        return print("You won, congratulations!")
    else:
        return print("You lost, try again!")
    

play(user, computer)