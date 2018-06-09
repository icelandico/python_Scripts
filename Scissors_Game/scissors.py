#Rock Paper Scissors program
import random
lst = ['rock', 'paper', 'scissors']
print ("\tPlay with computer this simple game\n\n"
       "\tYou can choose: \n\n"
       "\tRock\n"
       "\tPaper\n"
       "\tScissors\n"
       )

inp = "Exit"
while inp != "":
    computer = random.choice(lst)
    reka = input("\tWhat You choose ").lower()
    print ('\n')
    if computer == 'rock' and reka == 'scissors':
       print ("Computer has", '{}.'.format(computer),"You loose!\n")
       break

    elif computer == 'rock' and reka =='paper':
       print ("Computer has",'{}.'.format(computer),"You win!\n")
       break

    elif computer =='scissors' and reka =='rock':
        print ("Computer has",'{}.'.format(computer),"You win!\n")
        break

    elif computer == 'paper' and reka == 'rock':
        print ("Computer has",'{}.'.format(computer),"You loose!\n")
        break
    elif computer == 'paper' and reka == 'scissors':
        print ("Computer has",'{}.'.format(computer),"You win!\n")
        break
    elif computer == 'scissors' and reka == 'paper':
        print("Computer has", '{}.'.format(computer), "You loose!\n")
        break
    elif computer == reka:
        print ("Computer choose", '{}.'.format(computer),"Same as You! Try again.\n")
        continue
    else:
        print ("You have to choose one of items listed!\n")
        continue

print ("\n\t*** I hope You enjoyed this game ***\n")

input ("\t Press enter to exit the game.")

