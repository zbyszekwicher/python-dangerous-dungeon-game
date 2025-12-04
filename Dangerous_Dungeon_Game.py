import time
import script01
#import os; os.system("settings.py") -- super opcja
language = 'english'
inp_inp = ''

inp = input('if you want to go to settings, print "set"\n')
if inp == 'set':
        while not inp_inp == '0':
                if language == 'english':
                        inp_inp = input('\n1 - language\n2 - fight speed\n3 - difficulty\n0 - continue\n')
                        while not inp_inp in ('1','2','3','0'):
                                inp_inp = input('Thats incorect value. Type correct number\n')

                        if inp_inp == '1':
                            inp = input ('\nLANGUAGE\n1 - english\n2 - polski\n')
                            while not inp in ('1','2'):
                                inp = input('Thats incorect value. Type correct number\n')
                            if inp == '1':
                                language = 'english'
                            if inp == '2':
                                language = 'polski'
                        #        input('język zmieniony na polski\nkontynuuj\n')

                        if inp_inp == '2':
                            inp = input ('\nFIGHT SPEED\ntype value from 0 to 30\n(lower number = faster fight)\n')
                            dl = int(inp)/10
                            while not dl <= 3 or dl < 0:
                                inp = input('Thats incorect value. Type correct number')
                            script01.delay = dl

                        if inp_inp == '3':
                            if script01.difficulty == 1:
                                inp = input('\nDIFFICULTY\nYou are on the normal difficulty level. If you want to play on easy difficulty level type "easy". But then your score will not be saved.\n')
                                #time.sleep(0.2)

                            elif script01.difficulty == 0:
                                inp = input('\nDIFFICULTY\nYou are on the easy difficulty level. If you want to play on normal difficulty level type "normal". Remember that on easy level your score will not be saved.\n')
                                time.sleep(0.2)

                            if inp == 'easy':
                                    script01.difficulty = 0
                                    print ('\nDifficulty set to easy.\n')
                                    time.sleep(0.2)
                                    input ('continue')

                            if inp == 'normal':
                                    script01.difficulty = 1
                                    print ('\nDifficulty set to normal.\n')
                                    time.sleep(0.2)
                                    input ('continue')
                elif language == 'polski':
                        inp_inp = input('\n1 - jezyk\n2 - szybkosc walki\n3 - poziom trudnosci\n0 - kontynuuj\n')
                        while not inp_inp in ('1','2','3','0'):
                                inp_inp = input('To zla wartosc. Wpisz odpowiedni numer\n')

                        if inp_inp == '1':
                            inp = input ('\nJEZYK\n1 - english\n2 - polski\n')
                            while not inp in ('1','2'):
                                inp_inp = input('To zla wartosc. Wpisz odpowiedni numer\n')
                            if inp == '1':
                                language = 'english'
                            if inp == '2':
                                language = 'polski'

                        if inp_inp == '2':
                            inp = input ('\nSZYBKOSC WALKI\nwpisz wartosc od 0 do 30\n(mniejsza liczba = szybsza walka)\n')
                            dl = int(inp)/10
                            while not dl <= 3 or dl < 0:
                                inp_inp = input('To zla wartosc. Wpisz odpowiedni numer\n')
                            script01.delay = dl

                        if inp_inp == '3':
                            if script01.difficulty == 1:
                                inp = input('\nPOZIOM TRUDNOSCI\nJestes na normalnym poziomie trudnosci. Jesli chcesz grac na latwym poziomie trudnosci wpisz: "easy". Ale wtedy twoj wynik nie zostanie zapisany\n')
                                #time.sleep(0.2)

                            elif script01.difficulty == 0:
                                inp = input('\nPOZIOM TRUDNOSCI\nJestes na latwym poziomie trudnosci. Jesli chcesz grac na normalnym poziomie trudnosci wpisz "normal". Pamietaj, ze na latwym poziomie trudnosci twoj wynik nie zostanie zapisany.\n')
                                time.sleep(0.2)

                            if inp == 'easy':
                                    script01.difficulty = 0
                                    print ('\nPoziom trudnosci zmieniony na latwy\n')
                                    time.sleep(0.2)
                                    input ('kontynuuj')

                            if inp == 'normal':
                                    script01.difficulty = 1
                                    print ('\nPoziom trudnosci zmieniony na normalny\n')
                                    time.sleep(0.2)
                                    input ('kontynuuj')

input('\nS T A R T\n')

if language == 'english':
        import script2


if language == 'polski':
	import script2_polski
