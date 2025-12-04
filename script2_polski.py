input('Witaj w grze Dangerous Dungeon!')

import script1_polski as f
import sys
import random
import time

inp=()
while not inp:
	inp = input('Wpisz imię twojej postaci: ')
name = inp
maxLv = 1
hero = [name, (maxLv+4)*2]

def gameOver():
	print('\nZginąłeś w akcji zabity przez ' + f.killedBy+' na '+str(maxLv)+' poziomie.')
	time.sleep(0.2)
	input ('Przegrałeś')
	time.sleep(0.2)
	PrintScores()
	input('\nwyjdź\n')
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
	print ('\nWyszedłeś z podziemi.')
	time.sleep(0.2)
	value = 0
	if loot:
		print ('Twoje skarby:')
		for i in loot:
			time.sleep(0.2)
			print (i[0]+'\t wartość '+str(i[1]))
			value += i[1]
	else:
		print ('Niestety nie zebrałeś żadnych skarbów')
	time.sleep(0.2)
	print('twój wynik: (łączna wartość): '+str(value),'\n')
	
	if f.difficulty == 1:
		if value < 10:
			value = '0'+str(value)
			print (value)
	
		text = str(value)+'	'+name+' level '+str(maxLv)+' ; '
		file = open('highscores','a')
		file.write(text)
		file.close()
	else:
		print('Wynik nie został zapisany ponieważ grałeś na łatwym poziomie trudności')
		time.sleep(0.2)
		input('kontynuuj\n')
	
	PrintScores()
	input('\nwyjdź\n')
	sys.exit()

print('Hej, '+name+'. Jesteś przed wejściem do niebezpiecznych lochów')
time.sleep(0.2)
print('Twój poziom to: ', maxLv, ', i twoja siła to: ',hero[1])
time.sleep(0.2)
input('na przód!')

e1 = ['mały goblin wojownik', 1]
e2 = ['ork mag', 3]
e3 = ['goblin łucznik', 2]
e4 = ['mroczny szaman', 7]
e5 = ['pająk jaskiniowy',2]
e6 = ['wielki robal', 3]
e7 = ['ranny troll', 5]
e8 = ['gigantyczna mrówka', 3]  
e9 = ['ork z włucznią', 4]
e10 = ['ork z dwoma sztyletami', 5]
e11 = ['ork z maczugą',3]
e12 = ['duży goblin wojownik',4]
e13 = ['zwykły mutant',9]
e14 = ['wielki, gruby goblin z maczugą', 6]
e15 = ['ork łucznik', 4]
e16 = ['jadowity pająk', 7]
e17 = ['wielki wilczur', 8]
e18 = ['mroczny kultysta z fajną szablą', 9]
e19 = ['mroczny kultysta z rytualnym nożem', 8]
e20 = ['mroczny kultysta ale też magik', 9]
e21 = ['mroczny kultysta z wielką książką', 6]
e22 = ['Pięć wkurzonych goblinów atakujacych razem', 10]
e23 = ['głodny troll', 13]
e24 = ['szkielet z mieczem', 9]
e25 = ['szkielet z maczugą', 8]
e26 = ['szkielet z krwawym sztyletem',10]
e27 = ['szkielet z włucznią',11]
e28 = ['wielki goblin mutant',13]
e29 = ['hydra',15]

lv1enemy = [e1,e2,e3,e1,e5,e6,e1,e8,e9,e3,e11,e12,e15]
l1 = ['główna brama']
l2 = ['wielki hol']
dungStart = [l1, l2]
#at least 4 names per lv.
lv2Lname = ['duża jaskinia', 'kolejny ciemny pokój', 'małe podziemne jezioro','kolejny ciemny pokój']
lv2enemy = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e15]
lv2floors = []
lv3Lname = ['jaskinia z świecącymi grzybami','stara krasnoludzka kopalnia złota','schody do podziemi','komnata z głęboką studnią w podłodze']
lv3enemy = [e4,e7,e9,e12,e13,e13,e13,e14,e15,e16]
lv3floors  = []
lv4Lname = ['świątynia mrocznych kultystów','zakrwawiona komnata z kamiennym stołem','gabinet mrocznych kultystów z prawdziwym drewnianym stołem', 'cmentarzysko kości',]
lv4enemy = [e3,e13,e13,e18,e18,e19,e19,e19,19,e20,e21,e21,e21]
lv4floors = []
lv5Lname = ['znowu kolejne ciemne miejsce','znowu kolejne ciemne schody','... Czekaj! To jest prawdziwe podziemne miasto!','zimowa sypialnia trolli']
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
t_lv1 = [['brązowa moneta\t ',1],['stara zepsuta figurka',1],['metalowa branzoleta',1],['właściwie nic\t ',0]]
t_lv2 = [['srebrna moneta\t ',5],['metalowy pierścień ',2],['trzy brązowe monety',3],['kawałek starego sera',1]]
t_lv3 = [['złota moneta\t ',10],['siedem brązowych monet',7],['ostry nóż\t ',9],['złoty pierścień ',13],['mieszek pełen monet',14+r()],['dziwne kości\t ',0]]
t_lv4 = [['rytualny nóż\t ',18],['złota figura boga mrocznych kultystów',21],['trzy srebrne monety',15],['torba monet\t ',23+r()],['szesnaście brązowych monet',16]]
t_lv5 = [['dwie złote monety',20],['pięć srebrnych monet',25],['dwadzieścia trzy brązowe monety',23],['mała skrzynia monet',27+r()],['kamień runiczny',30+r()],['mały diament',35+r()],['mały szmaragd',25],['magiczny pierścień',32]]

t_lv2.extend(t_lv1)
t_lv3.extend(t_lv2)
t_lv4.extend(t_lv3)
t_lv5.extend(t_lv4)

def GetTreasure(t_lv):
	return t_lv[random.randrange(len(t_lv1))]

def LevelUp():
	print('\nNOWY POZIOM!\n')
	time.sleep(0.2)
	global maxLv
	maxLv += 1
	hero[1] = (maxLv+4)*2
	print('właśnie awansowałeś na nowy poziom. Teraz twój poziom to ', maxLv)
	time.sleep(0.2)
	print('i twoja siła to ',hero[1],'\n')
	time.sleep(0.2)
	input('kontynuuj\n')

def Gameplay(i,t_lv):
	print('twoim oczom ukazuje się '+i[0])
	time.sleep(0.2)
	print('widziesz ',len(i[1]),' przeciwników.')
	time.sleep(0.2)
	for y in i[1]:
		print (y[0])
		time.sleep(0.2)
	inp = input('Wpisz "esc" jeśli chcesz wyjść z podziemi\n')
	if inp == 'esc':
		escape()
	print('\nWięc teraz musisz walczyć!\n')
	time.sleep(0.2)
	for y in i[1]:
		f.fight(hero, y)
		hero[1] = f.herolv
		if hero[1] == 0:
			gameOver()
		print('\n')
	print('scena oczyszczona!')
	time.sleep(0.2)
	input('teraz jest czas na szukanie ukrytych skarbów!\n')
	findes = GetTreasure(t_lv)
	global loot
	loot.append(findes)
	print('przeszukiwanie...')
	time.sleep(random.randrange(10,30)/10)
	print('znalazłeś ' +findes[0])
	time.sleep(0.5)
	input('kontynuuj wycieczkę\n')

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


print('\nWszedłeś do ostatniej wielkeij jaskini. Nie ma już więcej lochów do eksploracji!!')
time.sleep(0.2)
print('Ale za to jest wielka skrzynia ze złotem i diamentami!')
time.sleep(0.2)
loot.append(['!FINAŁOWA SKRZYNIA!',100])
input ('Nic tu nie ma więcej do roboty, wynośmy się z tego miejsca')
escape()
