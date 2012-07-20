# -*- coding: UTF-8 -*-
import pygame
import time
import math
pygame.init()
font = pygame.font.Font(None, 100)
font2 = pygame.font.Font(None, 64)
fon = pygame.image.load('1.png')
go = False

def main():
	size = 840, 440
	screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | 	pygame.HWSURFACE)
	done = False
	go = False
	kolvo_start = 3
	doska = Doska(screen)
	sterzhni = Sterzhni(screen)
	game = game_status(screen, kolvo_start)
	disk = Disk(screen)
	minclick = game.minclick
	click = game.click	
	width = 230
	height = 440
	left = 0
	top = 0
	fl = 0
	ff = True
	z = 0
	b = 0
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN: 
				if event.key == 32:
					ff = not ff
				if event.key == pygame.K_RIGHT:
					if left >= 460:break
					left += 230
				elif event.key == pygame.K_LEFT:
					if left <= 0:break
					left -= 230
		screen.fill((255,255,255))
		screen.blit(fon, (0,0))
		doska.draw(screen)
		sterzhni.draw(screen)
		palka(screen)
		ramka2(screen, width, height, left, top)
		if ff:
			ramka(screen, width, height, left, top)
			disk.delit(disk.sp_disk_1)
			print disk.sp_disk_1
			disk.draw(disk.sp_disk_1,screen)
		#print("Main loop: " , ff)
		#print(z, ff, left, disk.kolvo_1, disk.kolvo_2, disk.kolvo_3)
		#disk.move(z, ff, left, disk.kolvo_1, disk.kolvo_2, disk.kolvo_3)
		#print("Move func called")
		disk.draw(disk.sp_disk_1,screen)
		disk.draw(disk.sp_disk_2,screen)
		disk.draw(disk.sp_disk_3,screen)
		disk.delit(disk.sp_disk_1)
		disk.draw(disk.sp_disk_1,screen)
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

class Sterzhni:
	def __init__(self,screen):
		self.razmer = 4, 405
		self.screen = screen
		left_1 = 113
		left_2 = 343
		left_3 = 563
		top = 15
		self.rect_1 = pygame.Rect((left_1,top),self.razmer)
		self.rect_2 = pygame.Rect((left_2,top),self.razmer)
		self.rect_3 = pygame.Rect((left_3,top),self.razmer)
	def draw(self,screen):
		pygame.draw.rect(screen,(179,77,77),self.rect_1)
		pygame.draw.rect(screen,(179,77,77),self.rect_2)
		pygame.draw.rect(screen,(179,77,77),self.rect_3)



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

class Disk():
	def __init__(self, screen):
		self.screen = screen
		self.kolvo_1 = 3
		self.kolvo_2 = 0
		self.kolvo_3 = 0
		self.sp_disk_1 = self.disk(self.kolvo_1)
		print self.sp_disk_1
		self. sp_disk_2 = []
		self.sp_disk_3 = []
		a = 0
		b = 0
		c = 0
		
	def disk(self,kolvo): #создает список дисков, которые будут созданы в самом начале.
		width = 210
		height = 20
		i = 0
		sp_disk_1 = []
		while i < kolvo:
			width = width - 10
			left = 15 + i*5
			top = 400 - i*21
			disk = pygame.Rect((left,top),(width, height))
			i +=1
			sp_disk_1.append(disk)
		return sp_disk_1	
		
			
	
	def disk_1(self, a, kolvo, sp_disk_1): #добавляет в список дисков диск, который сняли с другого стежня. в функцию передается количество дисков со стержня, с которого сняли диск.
		i = 0
		while i < kolvo:
			width = width - 10
			left = 245 + i*5
			i +=1
		top = 400 - a*21
		disk = pygame.Rect((left,top),(width, height))
		sp_disk_1.append(disk)
		a += 1
		return self.sp_disk_1
		
	def disk_2(self,b, kolvo, sp_disk_2): #аналогично disk_1 только добавляет  sp_disk_2.
		i = 0
		while i < kolvo:
			width = width - 10
			left = 245 + i*5
			i +=1
		top = 400 - b*21
		disk = pygame.Rect((left,top),(width, height))
		sp_disk_2.append(disk)
		b += 1
		return self.sp_disk_2
			
			
	def disk_3(self, c, kolvo, sp_disk_3): ##аналогично disk_1 только добавляет  sp_disk_2.
		width = 210
		height = 20
		i = 0
		while i < kolvo:
			width = width - 10
			left = 475 + i*5
			i +=1
		top = 400 - c*21
		disk = pygame.Rect((left,top),(width, height))
		sp_disk_3.append(disk)
		c +=1
		return self.sp_disk_3
		
	def move(self, z, fff, left, kolvo_1, kolvo_2, kolvo_3): #перемещение диска. принимает z(то есть захвачен диск или нет, по умолчанию = 0), f - нажат ли пробел, left - положение рамки. все остальное вроде понятно.
		s = 0 
		
		print("Move func: ", fff)
		if fff and z == 0:
			z = 0
			if left < 230:
				s = 1
				if self.kolvo_1 <= 0:
					self.kolvo_1 = 0
				else:
					self.kolvo_1 -= 1
					self.delit(self.sp_disk_2)
				return self.sp_disk_1
			if left >=230 and left < 460:
				s = 2
				if self.kolvo_2 <= 0:
					self.kolvo_2 = 0
				else:
					self.kolvo_2 -= 1
					self.delit(self.sp_disk_2)
				return self.sp_disk_2
			if left >=460 and left < 690:
				s = 3
				if self.kolvo_3 <= 0:
					self.kolvo_3 = 0
				else:
					self.kolvo_3 -= 1
					self.delit(self.sp_disk_3)
				return self.sp_disk_3
			
		if fff and z == 1:
			z = 0
			if left < 230:
				self.kolvo_1 += 1
				if s == 2:
					self.disk_1(a,self.kolvo_2,self.sp_disk_1)
				elif s == 3:
					self.disk_1(a,kolvo_3,self.sp_disk_1)
				elif s == 1:
					self.move(1, 0, left, self.kolvo_1, self.kolvo_2, self.kolvo_3)
				return self.sp_disk_1
			if left >=230 and left < 460:
				self.kolvo_2 += 1
				if s == 1:
					self.disk_1(a,self.kolvo_1,self.sp_disk_1)
				elif s == 3:
					self.disk_1(a,self.kolvo_3,self.sp_disk_1)
				elif s == 2:
					self.move(1, 0, left, self.kolvo_1, self.kolvo_2, self.kolvo_3)
				return self.sp_disk_2
			if left >=460 and left < 690:
				self.kolvo_3 += 1
				if s == 1:
					self.disk_1(a,self.kolvo_1,self.sp_disk_1)
				elif s == 2:
					self.disk_1(a,self.kolvo_2,self.sp_disk_1)
				elif s == 3:
					self.move(1, 0, left, self.kolvo_1, self.kolvo_2, self.kolvo_3)
				return self.sp_disk_3

	def delit(self, sp_disk): # удаляет из переданого списка дисков последний(верхний диск)
		sp_disk = sp_disk[:-1]
		return sp_disk
	
	def draw(self, sp_disk, screen): # получив список дисков, рисует.
		for disk in sp_disk:
			pygame.draw.rect(self.screen,(87,57,205),disk)
		
	
def ramka(screen, width, height, left, top):
	ramka = pygame.Rect((left,top),(width,height))
	pygame.draw.rect(screen,(255,0,0),ramka, 3)
			
def ramka2(screen, width, height, left, top):
	ramka = pygame.Rect((left,top),(width,height))
	pygame.draw.rect(screen,(0,255,0),ramka, 3)

def mmenu(go):
		menu5 = font.render(u'Ханойские башни', 1, (0, 0, 0))
		menupos = pygame.Rect(115,100,247,45)
		menu2 = font2.render(u'Играть', 1, (0, 0, 0))
		menupos2 = pygame.Rect(320, 300,154,45)
		width = 840
		height = 440
		screen_size = (width, height)
		screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
		done = False
		while not go:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
					go = True
				elif event.type == pygame.MOUSEMOTION:
					if menupos2.collidepoint(event.pos):
						menu2 = font2.render(u'Играть', 1, (255, 255, 10))
						menu5 = font.render(u'Ханойские башни', 1, (0, 0, 0))
						game = 1
					else:
						menu = font.render(u'Ханойские башни', 1, (0, 0, 0))
						menu2 = font2.render(u'Играть', 1, (0, 0, 0))
						game = 0
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if game == 1:
						go = True
						done = False
						main()
			screen.fill((255,255,255))
			screen.blit(fon, (0, 0))
			screen.blit(menu5, menupos)
			screen.blit(menu2, menupos2)
			pygame.display.flip()


mmenu(go)
