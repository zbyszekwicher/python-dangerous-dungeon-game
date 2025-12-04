import random
import time

difficulty = 1
delay = 0.7

def fight(f1, f2):
	lv1 = f1[1]
	lv2 = f2[1]
	def actRemis():
		global remis
		if lv1 < lv2:
			remis = lv1
		else:
			remis = lv2

	print(f1[0]+'('+str(lv1)+')'+ '  vs  '+'('+str(lv2)+')'+ f2[0])
	time.sleep(delay)
	
	hp1 = lv1
	hp2 = lv2
	
	if lv1 == 1:
		lv1 = 2
	if lv2 == 1:
		lv2 = 2
	
	actRemis()
	
	while hp1 != 0 and  hp2 != 0:
		r = random.randrange(lv1+lv2+remis)
		result = r+1;
		if result <= lv1:
			if difficulty == 0:
				critical = 1##ma byc 3
			else:
				critical = 10
			if random.randrange(critical) == 0:
				print(f1[0]+' deals a critical hit!')
				time.sleep(delay)
				print(f2[0]+' dies!')
				time.sleep(delay)
				hp2 = 0
			else:
				print(f1[0]+' hits!')
				time.sleep(delay)
				hp2 -=1
				if lv2 != 2:
					lv2 -= 1
			#print(f1[0]+' - ', lv1, f2[0]+' - ', lv2)
			if hp2 == 0:
				print(f1[0]+' won fight with ', hp1, 'power')
		elif result < lv1+lv2 or result == lv1+lv2:
			print(f2[0]+' hits!')
			time.sleep(delay)
			hp1 -=1
			if lv1 != 2:
				lv1 -= 1
			#print(f1[0]+' - ', lv1, f2[0]+' - ', lv2)
			if hp1== 0:
				print(f2[0]+' won fight with ', hp2, 'power')
				global killedBy
				killedBy = f2[0]
		else:
			print('draw')
		time.sleep(delay)
		actRemis()
	
	global herolv
	herolv = hp1


#enemies = [['goblin warrior',1],['goblin boss',4],['goblin archer',2]]
#while True:
#	fight(['hero',5], enemies[random.randrange(len(enemies))])