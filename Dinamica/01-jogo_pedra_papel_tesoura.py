import random
print("Let's start a play, rock, paper and scissors!")
user = input("What's your choise: rock, paper or scissors! ")
computer = random.choice(["rock", "paper", "scissors"])

#função que chama a partida
def play(user2, computer2):
    print("I chose: ", computer2)
    if user2 == computer2:
        return print("It's a tie!")
    quem_venceu(user2, computer2)

#função que define quem venceu
def quem_venceu(user1, computer1):
    if (user1 == "rock" and computer1 == "scissors") or (user1 == "scissors" and computer1 == "paper") \
        or (user1 =="paper" and computer1 == "rock"):
        return print("You won, congratulations!")
    else:
        return print("You lost, try again!")
    

play(user, computer)