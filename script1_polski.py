import script01
import random
import time

script01.difficulty = 1
script01.delay = 0.7

def fight(f1, f2):
	lv1 = f1[1]
	lv2 = f2[1]
	def actRemis():
		global remis
		if lv1 < lv2:
			remis = lv1
		else:
			remis = lv2

	print(f1[0]+'('+str(lv1)+')'+ '  kontra  '+'('+str(lv2)+')'+ f2[0])
	time.sleep(script01.delay)
	
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
			if script01.difficulty == 0:
				critical = 1##ma byc 3
			else:
				critical = 10
			if random.randrange(critical) == 0:
				print(f1[0]+' zadał KRYTYCZNY CIOS!')
				time.sleep(script01.delay)
				print(f2[0]+' umiera!')
				time.sleep(script01.delay)
				hp2 = 0
			else:
				print(f1[0]+' zadał cios!')
				time.sleep(script01.delay)
				hp2 -=1
				if lv2 != 2:
					lv2 -= 1
			#print(f1[0]+' - ', lv1, f2[0]+' - ', lv2)
			if hp2 == 0:
				print(f1[0]+' wygrał walkę z ', hp1, 'siły')
		elif result < lv1+lv2 or result == lv1+lv2:
			print(f2[0]+' zadał cios!')
			time.sleep(script01.delay)
			hp1 -=1
			if lv1 != 2:
				lv1 -= 1
			#print(f1[0]+' - ', lv1, f2[0]+' - ', lv2)
			if hp1== 0:
				print(f2[0]+' wygrał walkę z ', hp2, 'siły')
				global killedBy
				killedBy = f2[0]
		else:
			print('remis')
		time.sleep(script01.delay)
		actRemis()
	
	global herolv
	herolv = hp1
