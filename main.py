import random
from Player import Player

def rollDice():
	return random.randint(1,6)

def isEvenNum(number):
	mod = number % 2
	if mod > 0:
		return false
	else:
		return true

p1name = input("Player 1, enter your name: ")
p1 = Player(p1name, 0)

p2name = input("Player 2, enter your name: ")
p2 = Player(p2name, 0)

counter = 0
turn = True

while counter < 5:
	if turn:
		diceRoll = rollDice()
		print(p1.getName() + ' rolled ' + str(diceRoll))

		if isEvenNum:
			p1.addPoints(10)
		else:
			p1.removePoints(5)

		counter = counter + 1
		turn = False
	else:
		diceRoll = rollDice()
		print(p2.getName() + ' rolled ' + str(diceRoll))

		if isEvenNum:
			p2.addPoints(10)
		else:
			p2.removePoints(5)

		counter = counter + 1
		turn = True

print('Counter has finished')
print(p1.getName() + ' has got ' + str(p1.getPoints()))
print(p2.getName() + ' has got ' + str(p2.getPoints()))

if p1.getPoints() > p2.getPoints():
	print(p1.getName() + ' has won!')
else:
	print(p2.getName() + ' has won!')
	