input('Hello and wellcome to the Dangerous Dungeon game!')

import script01 as f
import sys
import random
import time

inp=()
while not inp:
	inp = input('Type your hero name: ')
name = inp
maxLv = 1
hero = [name, (maxLv+4)*2]

def gameOver():
	print('\nYou died in action killed by ' + f.killedBy+' at '+str(maxLv)+' level.')
	time.sleep(0.2)
	input ('Your game is over')
	time.sleep(0.2)
	PrintScores()
	input('\nexit\n')
	sys.exit()

def PrintScores():
	print('\nH I G H S C O R E S')
	time.sleep(0.2)
	file = open('highscores')
	scores = file.read()
	file.close()

	scr = scores.split(' ; ')
	scr.sort()
	scr.reverse()
	
	scoresLen = 10
	if len(scr) < scoresLen:
		for i in range(len(scr)):
			nr = str(i+1)
			print (nr+')	'+scr[i])
			time.sleep(0.2)
	else:
		for i in range(scoresLen):
			nr = str(i+1)
			print (nr+')	'+scr[i])
			time.sleep(0.2)

def escape():
	print ('\nYou left the dungeon.')
	time.sleep(0.2)
	value = 0
	if loot:
		print ('Your treasures:')
		for i in loot:
			time.sleep(0.2)
			print (i[0]+'\t value: '+str(i[1]))
			value += i[1]
	else:
		print ('Unfortunately you gain no treasures.')
	time.sleep(0.2)
	print('your score (total value): '+str(value),'\n')
	
	if f.difficulty == 1:
		if value < 10:
			value = '0'+str(value)
			print (value)
	
		text = str(value)+'	'+name+' level '+str(maxLv)+' ; '
		file = open('highscores','a')
		file.write(text)
		file.close()
	else:
		print('Score is not saved because you played on easy difficulty level')
		time.sleep(0.2)
		input('continue\n')
	
	PrintScores()
	input('\nexit\n')
	sys.exit()

print('Hi, '+name+'. You are in front of the Dangerous Dungeon!')
time.sleep(0.2)
print('your level is ', maxLv, ', and your power is ',hero[1])
time.sleep(0.2)
input('lets go into!')

e1 = ['small goblin warrior', 1]
e2 = ['orc mage', 3]
e3 = ['goblin archer', 2]
e4 = ['dark shaman', 7]
e5 = ['cave spider',2]
e6 = ['large insect', 3]
e7 = ['hurted troll', 5]
e8 = ['biggest ant you have ever seen', 3]  
e9 = ['orc with a spear', 4]
e10 = ['orc with two knifes', 5]
e11 = ['orc with a mace',3]
e12 = ['big goblin warrior',4]
e13 = ['common mutant',9]
e14 = ['huge, fat goblin with mace', 6]
e15 = ['orc archer', 4]
e16 = ['poison spider', 7]
e17 = ['big wolf', 8]
e18 = ['death cultist with nice saber', 9]
e19 = ['death cultist with his ritual knife', 8]
e20 = ['death cultist but also mage', 9]
e21 = ['death cultist holding huge ritual book', 6]
e22 = ['five angry goblins. They are atacking at once', 10]
e23 = ['hungry troll', 13]
e24 = ['skeleton with a sword', 9]
e25 = ['skeleton with a mace', 8]
e26 = ['skeleton with a bloody knife',10]
e27 = ['skeleton with a spear',11]
e28 = ['big goblin mutant',13]
e29 = ['hydra',15]

lv1enemy = [e1,e2,e3,e1,e5,e6,e1,e8,e9,e3,e11,e12,e15]
l1 = ['main gate']
l2 = ['big hall']
dungStart = [l1, l2]
#at least 4 names per lv.
lv2Lname = ['large cave', 'just another dark room', 'small undeground lake','just another dark room']
lv2enemy = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e15]
lv2floors = []
lv3Lname = ['cave of lightning mushroms','old dwarfen gold mine','stairs to the undeground','room with kind of a big whole in the floor']
lv3enemy = [e4,e7,e9,e12,e13,e13,e13,e14,e15,e16]
lv3floors  = []
lv4Lname = ['big temple of death cultists','bloody room with stone table','death cultist s office with real wooden table', 'cementery of bones',]
lv4enemy = [e3,e13,e13,e18,e18,e19,e19,e19,19,e20,e21,e21,e21]
lv4floors = []
lv5Lname = ['yet another dark place','yet andother dark stairs','... Whait! Thats a real undeground city!','Trolls winter bedroom']
lv5enemy = [e13, e13, e17,e22,e23,e24,e25,e26,e27,e28]
lv5floors = []

x = []
for i in range(2):
        x.append(lv1enemy[random.randrange(len(lv1enemy))])
l1.append(x)
x = []
for i in range(2):
        x.append(lv1enemy[random.randrange(len(lv1enemy))])
l2.append(x)

loot = []
def r():
	return random.randrange(-3,4)
t_lv1 = [['bronze coin\t ',1],['old, damaged figure',1],['metal bransolete',1],['quite nothing\t ',0]]
t_lv2 = [['silver coin\t ',5],['metal ring\t ',2],['three bronze coins',3],['piece of old cheese',1]]
t_lv3 = [['gold coin\t ',10],['seven bronze coins',7],['sharp knife\t ',9],['gold ring\t ',13],['pocket full of coins',14+r()],['strange bones\t ',0]]
t_lv4 = [['ritual knife\t ',18],['golden statue of cultists god',21],['three silver coins',15],['bag of coins\t ',23+r()],['sixteen bronze coins',16]]
t_lv5 = [['two golden coins',20],['five silver coins',25],['twenty three bronze coins',23],['small chest of coins',27+r()],['rune stone',30+r()],['small dimond',35+r()],['small emerald',25],['magic ring',32]]

t_lv2.extend(t_lv1)
t_lv3.extend(t_lv2)
t_lv4.extend(t_lv3)
t_lv5.extend(t_lv4)

def GetTreasure(t_lv):
	return t_lv[random.randrange(len(t_lv1))]

def LevelUp():
	print('\nLEVEL UP!\n')
	time.sleep(0.2)
	global maxLv
	maxLv += 1
	hero[1] = (maxLv+4)*2
	print('you have just leveld up. Now your level is ', maxLv)
	time.sleep(0.2)
	print('and your power is ',hero[1],'\n')
	time.sleep(0.2)
	input('continue\n')

def Gameplay(i,t_lv):
	print('You are at the '+i[0])
	time.sleep(0.2)
	print('You see ',len(i[1]),' enemies.')
	time.sleep(0.2)
	for y in i[1]:
		print (y[0])
		time.sleep(0.2)
	inp = input('Type "esc" if you want to escape from the dungeon\n')
	if inp == 'esc':
		escape()
	print('\nSo, now you have to fight!\n')
	time.sleep(0.2)
	for y in i[1]:
		f.fight(hero, y)
		hero[1] = f.herolv
		if hero[1] == 0:
			gameOver()
		print('\n')
	print('you cleard the stage!')
	time.sleep(0.2)
	input('now its time to look for some hidden treasures!\n')
	findes = GetTreasure(t_lv)
	global loot
	loot.append(findes)
	print('searching...')
	time.sleep(random.randrange(10,30)/10)
	print('you found ' +findes[0])
	time.sleep(0.5)
	input('continue your trip\n')

def NewLevelSetup(name,enemy,level,x):
	for i in range(random.randrange(3)+2):
		lista1 = []
		lista1.append(name.pop(random.randrange(len(name))))
		lista2 = []
		for i in range(random.randrange(x)+1):
			lista2.append(enemy[random.randrange(len(enemy))])
		lista1.append(lista2)
		level.append(lista1)
		
for i in dungStart:
	Gameplay(i,t_lv1)
		
LevelUp()
NewLevelSetup(lv2Lname,lv2enemy,lv2floors,4)
for i in lv2floors:
	Gameplay(i,t_lv2)

LevelUp()
NewLevelSetup(lv3Lname,lv3enemy,lv3floors,3)
for i in lv3floors:
	Gameplay(i,t_lv3)

LevelUp()
NewLevelSetup(lv4Lname,lv4enemy,lv4floors,3)
for i in lv4floors:
	Gameplay(i,t_lv4)
	
LevelUp()
NewLevelSetup(lv5Lname,lv5enemy,lv5floors,3)
for i in lv5floors:
	Gameplay(i,t_lv4)


print('\nYou have got into a big cave. There is no more dungeon to explore!!')
time.sleep(0.2)
print('But there is big chest full of dimonds and gold!')
time.sleep(0.2)
loot.append(['final chest',100])
input ('Nothing left to do. Lets get out of here')
escape()
