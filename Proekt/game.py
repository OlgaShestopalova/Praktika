# -*- coding: UTF-8 -*-
import pygame
import time
import sys
pygame.init()
font = pygame.font.Font(None, 100)
font2 = pygame.font.Font(None, 64)
font3 = pygame.font.Font(None, 32)
font4 = pygame.font.Font(None, 40)
fon = pygame.image.load('1.png')
pygame.mixer.music.load('igra.mp3')
sound_on = pygame.image.load('note.png')
sound_off = pygame.image.load('note2.png')
bronza = pygame.image.load('bronza.png')
serebro = pygame.image.load('serebro.png')
zoloto = pygame.image.load('zoloto.png')
instr = pygame.image.load('instr.png')
go = False
kolvo_start = 3

def main():
	size = 840, 440
	screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | 	pygame.HWSURFACE)
	done = False
	global kolvo_start
	doska = Doska(screen)
	color = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (30, 144, 255), (0, 0, 255), (160, 32, 240)]
	st_1 = Sterzhni_1(screen, kolvo_start, color)
	st_2 = Sterzhni_2(screen)
	st_3 = Sterzhni_3(screen)
	game = game_status(screen, kolvo_start)
	minclick = game.minclick
	click = game.click	
	width = 230
	height = 440
	left = 0
	top = 0
	ff = 0
	win = False
	s = 0
	muz = 0
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.MOUSEMOTION:
				mx, my = event.pos
			if event.type == pygame.KEYDOWN: 
				if event.key == 32 and ff == 0:
					while win == False:
						if left == 0:
							s = 1
						if left == 230:
							s = 2
						if left == 460:
							s = 3
						win = True
					ff = 1
				elif event.key == 32 and ff == 1:
					while win == True:
						if left == 0:
							ss = 1
						if left == 230:
							ss = 2
						if left == 460:
							ss = 3
						win = False
					ff = 0
					move(s, ss, st_1, st_2, st_3, st_1.kolvo_1, st_2.kolvo_2, st_3.kolvo_3, st_1.sp_disk_1, st_2.sp_disk_2, st_3.sp_disk_3, game)								
					if st_3.kolvo_3 == kolvo_start:
						wwin(go, game)
				if event.key == pygame.K_RIGHT:
					if left >= 460:break
					left += 230
				elif event.key == pygame.K_LEFT:
					if left <= 0:break
					left -= 230
			if event.type == pygame.MOUSEBUTTONDOWN:
				if mx > 710 and mx <756 and my > 380 and my < 430 and muz == 0:
					pygame.mixer.music.pause()
					muz = 1
				elif mx > 710 and mx <756 and my > 380 and my < 430 and muz == 1:
					pygame.mixer.music.unpause()
					muz = 0
					
			text1 = font3.render('Click ' + str(game.click), 1, (0,0,0))
			textpos1 = text1.get_rect()
			textpos1 = (720, 50)
			text2 = font3.render('Minclick ' + str(game.minclick), 1, (0,0,0))
			textpos2 = text1.get_rect()
			textpos2 = (700, 150)
			
		screen.fill((255,255,255))
		screen.blit(fon, (0,0))
		screen.blit(sound_on,(710,380))
		if muz == 0:
			screen.blit(sound_on,(710,380))
		elif muz == 1:
			screen.blit(sound_off,(710,380))
				
		doska.draw(screen)
		st_1.draw(screen)
		st_2.draw(screen)
		st_3.draw(screen)
		screen.blit(text1, textpos1)
		screen.blit(text2, textpos2)
		palka(screen)
		ramka(screen, width, height, left, top)
		if ff == 1:
			ramka2(screen, width, height, left, top)
		draw(st_1.sp_disk_1,screen)
		draw(st_2.sp_disk_2,screen)
		draw(st_3.sp_disk_3,screen)
		
		pygame.display.flip()

		time.sleep(0.015)


class Doska:
	def __init__(self,screen):
		self.razmer = 690, 20
		left = 0
		top = 420
		self.screen = screen
		self.rect=pygame.Rect((left,top),self.razmer)
	def draw(self,screen):
		pygame.draw.rect(screen,(138,133,117),self.rect)

class Sterzhni_1:
	def __init__(self,screen,kolvo_start, color):
		self.razmer = 4, 405
		self.screen = screen
		self.color = color
		left_1 = 118
		top = 15
		self.rect_1 = pygame.Rect((left_1,top),self.razmer)
		self.kolvo_1 = kolvo_start
		self.sp_disk_1 = self.disk(self.kolvo_1, self.color)
		
	def draw(self,screen):
		pygame.draw.rect(screen,(179,77,77),self.rect_1)
		
	def disk(self, kolvo, color): #Создается список дисков для 1 стержня
		width = 200
		height = 57
		i = 0
		self.sp_disk_1 = []
		while i < kolvo:
			width = width - 20
			left = 118 - width/2
			top = 363 - i*58
			disk = pygame.Rect((left,top),(width, height))
			self.sp_disk_1.append((disk, self.color[i]))
			i +=1
		return self.sp_disk_1	
		
	def dell(self, kolvo_1, sp_disk_1): #Функция, уменьшающая количество дисков на 1 стержне.
		if self.kolvo_1 <= 0:
			self.kolvo_1 = 0
		else:
			self.kolvo_1 -= 1
			delete_1(self,self.sp_disk_1) 
		return sp_disk_1
	
		
	
def delete_1(st_1, sp_disk_1): #Функция, удаяляющая верхний диск из списка дисков на 1 стержне
	st_1.sp_disk_1 = st_1.sp_disk_1[:-1]
	return st_1.sp_disk_1
	
def delete_2(st_2,sp_disk_2):
	st_2.sp_disk_2 = st_2.sp_disk_2[:-1] #Функция, удаяляющая верхний диск из списка дисков на 2 стержне
	return st_2.sp_disk_2

def delete_3(st_3,sp_disk_3): #Функция, удаяляющая верхний диск из списка дисков на 3 стержне
	st_3.sp_disk_3 = st_3.sp_disk_3[:-1]
	return st_3.sp_disk_3
					
def preo(sp_disk, kolvo): #Функция, позволяющая получить из последнего элмента списка дисков его размеры
	if kolvo == 0:
		pass
	else:
		d = sp_disk[kolvo-1]
		c = d[0]
		width = c[2]
		height = c[3]
		sp = width, height
		return sp
						
class Sterzhni_2:
	def __init__(self,screen):
		self.razmer = 4, 405
		self.screen = screen
		left_2 = 343
		top = 15
		self.rect_2 = pygame.Rect((left_2,top),self.razmer)
		self.sp_disk_2 = []
		self.kolvo_2 = 0
		
	def draw(self,screen):
		pygame.draw.rect(screen,(179,77,77),self.rect_2)
	
	def dell(self, kolvo_2, sp_disk_2): #Функция, уменьшающая количество дисков на 2 стержне.
		if self.kolvo_2 <= 0:
			self.kolvo_2 = 0
		else:
			self.kolvo_2 -= 1
			delete_2(self, self.sp_disk_2)
		return sp_disk_2
	
	
class Sterzhni_3:
	def __init__(self,screen):
		self.razmer = 4, 405
		self.screen = screen
		left_3 = 568
		top = 15
		self.rect_3 = pygame.Rect((left_3,top),self.razmer)
		self.sp_disk_3 =[]
		self.kolvo_3 = 0
		
	def draw(self,screen):
		pygame.draw.rect(screen,(179,77,77),self.rect_3)
		
	def dell(self, kolvo_3, sp_disk_3):#Функция, уменьшающая количество дисков на 1 стержне.
		if self.kolvo_3 <= 0:
			self.kolvo_3 = 0
		else:
			self.kolvo_3 -= 1
			delete_3(self, self.sp_disk_3)
		return sp_disk_3
	

def palka(screen): 
	width = 2
	height = 440
	left = 690
	top = 0
	palka = pygame.Rect((left,top),(width,height))
	pygame.draw.rect(screen,(0,0,0),palka)

	
class game_status():
	def __init__(self, screen, kolvo):
		self.screen = screen
		self.kolvo = kolvo
		self.minclick = 2**self.kolvo-1
		self.click = 0
	
def draw(sp_disk, screen): #Получив список дисков, функция рисует диски
	if len(sp_disk) == 0: pass
	else:
		for i in range(len(sp_disk)):
			d = sp_disk[i]
			rect = d[0]
			color = d[1]
			pygame.draw.rect(screen, color, rect)
		
	
def ramka(screen, width, height, left, top): #Создание рамки зеленого цвета
	ramka = pygame.Rect((left,top),(width,height))
	pygame.draw.rect(screen,(0,255,0),ramka, 3)
			
def ramka2(screen, width, height, left, top):
	ramka = pygame.Rect((left,top),(width,height)) #Создание рамки красного цвета
	pygame.draw.rect(screen,(255,0,0),ramka, 3)

def menu(go):
		pygame.mixer.music.play(-1)
		pygame.display.set_caption('Ханойские башни')
		menu1 = font.render(u'Ханойские башни', 1, (0, 0, 0))
		menupos1 = pygame.Rect(115,100,500,45)
		menu2 = font2.render(u'Играть', 1, (0, 0, 0))
		menupos2 = pygame.Rect(330, 330,154,45)
		menu3 = font2.render(u'Инструкция', 1, (0, 0, 0))
		menupos3 = pygame.Rect(275, 270,280,45)
		menu4 = font3.render(u'Назад', 1, (0, 0, 0))
		menupos4 = pygame.Rect(700, 400, 154, 45)
		width = 840
		height = 440
		screen_size = (width, height)
		screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
		done = False
		inst = 0
		while not go:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.MOUSEMOTION:
					if menupos2.collidepoint(event.pos):
						menu2 = font2.render(u'Играть', 1, (255, 255, 10))
						menu1 = font.render(u'Ханойские башни', 1, (0, 0, 0))
						menu3 = font2.render(u'Инструкция', 1, (0, 0, 0))
						ggame = 1
					elif menupos3.collidepoint(event.pos) and inst == 0:
						menu3 = font2.render(u'Инструкция', 1, (255, 255, 10))
						menu1 = font.render(u'Ханойские башни', 1, (0, 0, 0))
						menu2 = font2.render(u'Играть', 1, (0, 0, 0))
						ggame = 2
					elif menupos4.collidepoint(event.pos) and inst == 1:
						menu4 = font3.render(u'Назад', 1, (255, 255, 10))
						ggame = 3
					else:
						menu1 = font.render(u'Ханойские башни', 1, (0, 0, 0))
						menu2 = font2.render(u'Играть', 1, (0, 0, 0))
						menu3 = font2.render(u'Инструкция', 1, (0, 0, 0))
						menu4 = font3.render(u'Назад', 1, (0, 0, 0))
						ggame = 0
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if ggame == 1:
						go = True
						done = False
						main()
					if ggame == 2:
						inst = 1
					if ggame == 3:
						inst = 0
						
			screen.fill((255,255,255))
			screen.blit(fon, (0, 0))
			if inst == 1:
				screen.blit(instr, (0,0))
				screen.blit(menu4, menupos4)
			else:
				screen.blit(menu1, menupos1)
				screen.blit(menu2, menupos2)
				screen.blit(menu3, menupos3)
			pygame.display.flip()


def move(s, ss, st_1, st_2, st_3, kolvo_1, kolvo_2, kolvo_3, sp_disk_1, sp_disk_2, sp_disk_3, game): #Функция перемещения дисков.
	if s == 1: #Если "захвачен" диск на 1 стержне.
		if st_1.kolvo_1 == 0: pass
		else:
			sp = preo(st_1.sp_disk_1, st_1.kolvo_1) #Получаем размеры верхнего диска на 1 стрежне
			c = st_1.sp_disk_1[st_1.kolvo_1 - 1]
			a = c[1] #Получаем цвет этого диска
			if ss == 1:
				return st_1.sp_disk_1
			st_1.dell(st_1, sp_disk_1) #Удаляем из списка дисков 1 стрежня верхний диск
			if ss == 2: #Если "опускаем" диск на 2 стержень
				sp1 = preo(st_2.sp_disk_2, st_2.kolvo_2) #Получаем размеры верхнего диска на 2 стержне
				if st_2.kolvo_2 == 0: #Если нет там дисков, добавляем в список дисков этот перемещенный диск.
					left = 343 - sp[0]/2
					top = 363 - kolvo_2*58
					disk = pygame.Rect((left,top), sp)
					st_2.sp_disk_2.append((disk, a))
					st_2.kolvo_2 += 1
					game.click += 1
					return st_2.sp_disk_2
				if sp1[0] > sp[0]: #Если размеры перемещаяемого диска меньше размеров верхнего диска на 2 стержне, добавляем его в список дисков.
					left = 343 - sp[0]/2
					top = 363 - kolvo_2*58
					disk = pygame.Rect((left,top), sp)
					st_2.sp_disk_2.append((disk, a))
					st_2.kolvo_2 += 1
					game.click += 1
					return st_2.sp_disk_2
				else: #В противном случае, возвращаем обратно в список дисков 1 стержня
					left = 118 - sp[0]/2
					top = 363 - (kolvo_1-1)*58
					disk = pygame.Rect((left,top), sp)
					st_1.sp_disk_1.append((disk, a))
					st_1.kolvo_1 += 1
					return st_1.sp_disk_1
			if ss == 3:
				sp1 = preo(st_3.sp_disk_3, st_3.kolvo_3)
				if st_3.kolvo_3 == 0:
					left = 568 - sp[0]/2
					top = 363 - kolvo_3*58
					disk = pygame.Rect((left,top), sp)
					st_3.sp_disk_3.append((disk,a))
					st_3.kolvo_3 += 1
					game.click += 1
					return st_3.sp_disk_3
				if sp1[0] > sp[0]:
					left = 568 - sp[0]/2
					top = 363 - kolvo_3*58
					disk = pygame.Rect((left,top), sp)
					st_3.sp_disk_3.append((disk, a))
					st_3.kolvo_3 += 1
					game.click += 1
					return st_3.sp_disk_3
				else: 
					left = 118 - sp[0]/2
					top = 363 - (kolvo_1-1)*58
					disk = pygame.Rect((left,top), sp)
					st_1.sp_disk_1.append((disk,a))
					st_1.kolvo_1 += 1
					return st_1.sp_disk_1
	if s == 2:
		if st_2.kolvo_2 == 0: pass
		else:
			sp = preo(st_2.sp_disk_2, st_2.kolvo_2)
			c = st_2.sp_disk_2[st_2.kolvo_2 - 1]
			a = c[1]
			if ss == 2:
				return st_2.sp_disk_2
			st_2.dell(st_2, sp_disk_2)
			if ss == 1:
				sp1 = preo(st_1.sp_disk_1, st_1.kolvo_1)
				if st_1.kolvo_1 == 0:
					left = 118 - sp[0]/2
					top = 363 - kolvo_1*58
					disk = pygame.Rect((left,top), sp)
					st_1.sp_disk_1.append((disk, a))
					st_1.kolvo_1 += 1
					game.click += 1
					return st_1.sp_disk_1
				if sp1[0] > sp[0]:
					left = 118 - sp[0]/2
					top = 363 - kolvo_1*58
					disk = pygame.Rect((left,top), sp)
					st_1.sp_disk_1.append((disk, a))
					st_1.kolvo_1 += 1
					game.click += 1
					return st_1.sp_disk_1
				else: 
					left = 343 - sp[0]/2
					top = 363 - (kolvo_2-1)*58
					disk = pygame.Rect((left,top), sp)
					st_2.sp_disk_2.append((disk, a))
					st_2.kolvo_2 += 1
					return st_2.sp_disk_2
			if ss == 3:
				sp1 = preo(st_3.sp_disk_3, st_3.kolvo_3)
				if st_3.kolvo_3 == 0:
					left = 568 - sp[0]/2
					top = 363 - kolvo_3*58
					disk = pygame.Rect((left,top), sp)
					st_3.sp_disk_3.append((disk,a))
					st_3.kolvo_3 += 1
					game.click += 1
					return st_3.sp_disk_3
				if sp1[0] > sp[0]:
					left = 568 - sp[0]/2
					top = 363 - kolvo_3*58
					disk = pygame.Rect((left,top), sp)
					st_3.sp_disk_3.append((disk,a))
					st_3.kolvo_3 += 1
					game.click += 1
					return st_3.sp_disk_3
				else: 
					left = 343 - sp[0]/2
					top = 363 - (kolvo_2-1)*58
					disk = pygame.Rect((left,top), sp)
					st_2.sp_disk_2.append((disk,a))
					st_2.kolvo_2 += 1
					return st_2.sp_disk_2
		
	if s == 3:
		if st_3.kolvo_3 == 0: pass
		else:
			sp = preo(st_3.sp_disk_3, st_3.kolvo_3)
			c = st_3.sp_disk_3[st_3.kolvo_3 - 1]
			a = c[1]
			if ss == 3:
				return st_3.sp_disk_3
			st_3.dell(st_3, sp_disk_3)
			if ss == 1:
				sp1 = preo(st_1.sp_disk_1, st_1.kolvo_1)
				if st_1.kolvo_1 == 0:
					left = 118 - sp[0]/2
					top = 363 - kolvo_1*58
					disk = pygame.Rect((left,top), sp)
					st_1.sp_disk_1.append((disk,a))
					st_1.kolvo_1 += 1
					game.click += 1
					return st_1.sp_disk_1
				if sp1[0] > sp[0]:
					left = 118 - sp[0]/2
					top = 363 - kolvo_1*58
					disk = pygame.Rect((left,top), sp)
					st_1.sp_disk_1.append((disk, a))
					st_1.kolvo_1 += 1
					game.click += 1
					return st_1.sp_disk_1
				else: 
					left = 568 - sp[0]/2
					top = 363 - (kolvo_3-1)*58
					disk = pygame.Rect((left,top), sp)
					st_3.sp_disk_3.append((disk,a))
					st_3.kolvo_3 += 1
					return st_3.sp_disk_3
			if ss == 2:
				sp1 = preo(st_2.sp_disk_2, st_2.kolvo_2)
				if st_2.kolvo_2 == 0:
					left = 343 - sp[0]/2
					top = 363 - kolvo_2*58
					disk = pygame.Rect((left,top), sp)
					st_2.sp_disk_2.append((disk,a))
					st_2.kolvo_2 += 1
					game.click += 1
					return st_2.sp_disk_2
				if sp1[0] > sp[0]:
					left = 343 - sp[0]/2
					top = 363 - kolvo_2*58
					disk = pygame.Rect((left,top), sp)
					st_2.sp_disk_2.append((disk,a))
					st_2.kolvo_2 += 1
					game.click += 1
					return st_2.sp_disk_2
				else: 
					left = 568 - sp[0]/2
					top = 363 - (kolvo_3-1)*58
					disk = pygame.Rect((left,top), sp)
					st_3.sp_disk_3.append((disk,a))
					st_3.kolvo_3 += 1
					return st_3.sp_disk_3
			
def wwin(go, game):
	menu1 = font3.render(u'Следующий уровень', 1, (0, 0, 0))
	menupos1 = pygame.Rect(600,380,300,45)
	menu2 = font3.render(u'Выход', 1, (0, 0, 0))
	menupos2 = pygame.Rect(750,340,154,45)
	menu3 = font.render(u'Конец!', 1, (0, 0, 0))
	menupos3 = pygame.Rect(170, 370,154,45)
	width = 840
	height = 440
	click = game.click
	minclick = game.minclick
	screen_size = (width, height)
	screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
	done = False
	global kolvo_start
	while not go:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.MOUSEMOTION:
				if menupos2.collidepoint(event.pos):
					menu2 = font3.render(u'Выход', 1, (255, 255, 10))
					menu1 = font3.render(u'Следующий уровень', 1, (0, 0, 0))
					game = 1
				elif menupos1.collidepoint(event.pos):
					menu1 = font3.render(u'Следующий уровень', 1, (255, 255, 10))
					menu2 = font3.render(u'Выход', 1, (0, 0, 0))
					game = 2
				else:
					menu1 = font3.render(u'Следующий уровень', 1, (0, 0, 0))
					menu2 = font3.render(u'Выход', 1, (0, 0, 0))
					game = 0
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if game == 1:
					sys.exit(0)
				if game == 2:
					done = False
					go = True
					kolvo_start += 1
					if kolvo_start >7:
						exitt(game)
						break
					else:		
						main()

		
		text1 = font4.render('Click ' + str(click), 1, (0,0,0))
		textpos1 = text1.get_rect()
		textpos1 = (680, 190)
		text2 = font4.render('MinClick ' + str(minclick), 1, (0,0,0))
		textpos2 = text2.get_rect()
		textpos2 = (680, 150)	
		
		screen.fill((210,210,255))
		screen.blit(fon, (0,0))
		if click - minclick < 10:
			screen.blit(zoloto, (50, 0))
		elif click - minclick > 10 and click - minclick < 50:
			screen.blit(serebro, (50,0))
		else:
			screen.blit(bronza,(50,0))
		screen.blit(menu2, menupos2)
		screen.blit(text1, textpos1)
		screen.blit(text2, textpos2)
		screen.blit(menu1, menupos1)	
		pygame.display.flip()
	time.sleep(0.015)

def exitt(game_status):
	menu2 = font3.render(u'Выход', 1, (0, 0, 0))
	menupos2 = pygame.Rect(710, 370,154,45)
	menu = font.render(u'Игра окончена', 1, (0, 0, 0))
	menupos = pygame.Rect(160, 150,154,45)
	width = 840
	height = 440
	screen_size = (width, height)
	screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
	done = False
	global kolvo_start
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.MOUSEMOTION:
				if menupos2.collidepoint(event.pos):
					menu2 = font3.render(u'Выход', 1, (255, 255, 10))
					menu = font.render(u'Игра окончена', 1, (0, 0, 0))
					game = 1
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if game == 1:
					sys.exit(0)
		
		screen.fill((255,255,255))
		screen.blit(fon, (0, 0))
		screen.blit(menu2, menupos2)
		screen.blit(menu, menupos)
		pygame.display.flip()
	time.sleep(0.015)
	
menu(go)


