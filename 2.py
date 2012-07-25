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
	st_1 = Sterzhni_1(screen)
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
	sp = 0
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN: 
				if event.key == 32 and ff == 0:
					while win == False:
						if left == 0:
							s = 1
							
							st_1.dell(st_1.kolvo_1, st_1.sp_disk_1)
							print st_1.sp_disk_1
							draw(st_1.sp_disk_1,screen)
							win = True
						if left == 230:
							sp_2 = preo(st_2.sp_disk_2,st_2.kolvo_1)
							st_2.dell(st_2.kolvo_2, st_2.sp_disk_2)
							s = 2
						if left == 460:
							sp_3 = preo(st_3.sp_disk_3,st_3.kolvo_1)
							st_3.dell(st_3.kolvo_3, st_3.sp_disk_3)
							s = 3
					ff = 1
				elif event.key == 32 and ff == 1:	
					while win == True:		
						if ff == True:
							if left == 0:
								st_1.add(s, st_2, st_3, st_1.kolvo_1, st_2.kolvo_2, st_3.kolvo_3)
								win = False
							if left == 230:
								st_2.add(s, st_1, st_3, st_1.kolvo_1, st_2.kolvo_2, st_3.kolvo_3, sp_2)
								win = False
							if left == 460:
								st_3.add(s, st_2, st_1, st_1.kolvo_1, st_2.kolvo_2, st_3.kolvo_3)
								win = False
					ff = 0								
				if event.key == pygame.K_RIGHT:
					if left >= 460:break
					left += 230
				elif event.key == pygame.K_LEFT:
					if left <= 0:break
					left -= 230
		screen.fill((255,255,255))
		screen.blit(fon, (0,0))
		doska.draw(screen)
		st_1.draw(screen)
		st_2.draw(screen)
		st_3.draw(screen)
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
	def __init__(self,screen):
		self.razmer = 4, 405
		self.screen = screen
		left_1 = 113
		top = 15
		self.rect_1 = pygame.Rect((left_1,top),self.razmer)
		self.kolvo_1 = 3
		self.sp_disk_1 = self.disk(self.kolvo_1)
		self.a = 0
		
	def draw(self,screen):
		pygame.draw.rect(screen,(179,77,77),self.rect_1)
		
	def disk(self,kolvo): 
		width = 210
		height = 20
		i = 0
		self.sp_disk_1 = []
		while i < kolvo:
			width = width - 10
			left = 15 + i*5
			top = 400 - i*21
			disk = pygame.Rect((left,top),(width, height))
			i +=1
			self.sp_disk_1.append(disk)
		return self.sp_disk_1	
	
	def dell(self, kolvo_1, sp_disk_1):
		if self.kolvo_1 <= 0:
			self.kolvo_1 = 0
		else:
			self.kolvo_1 -= 1
			delete_1(self,self.sp_disk_1)

	def add(self, s, st_2, st_3, kolvo_1, kolvo_2, kovlo_3):
		self.kolvo_1 += 1
		if s == 2:
			self.disk_1(self.a,st_2.kolvo_2,self.sp_disk_1, sp)
		elif s == 3:
			self.disk_1(self.a,st_3.kolvo_3,self.sp_disk_1, sp)
		elif s == 1:
			pass
		return self.sp_disk_1
	
def delete_1(st_1, sp_disk_1): 
	st_1.sp_disk_1 = st_1.sp_disk_1[:-1]
	return st_1.sp_disk_1
	
def delete_2(st_2,sp_disk_2):
	st_2.sp_disk_2 = st_2.sp_disk_2[:-1]
	return st_2.sp_disk_2

def delete_3(st_3,sp_disk_3):
	st_3.sp_disk_3 = st_3.sp_disk_3[:-1]
	return st_3.sp_disk_3
					
def preo(sp_disk, kolvo): 
	d = sp_disk[kolvo-1]
	print d
	width = d[2]
	height = d[3]
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
		self.b = 0
		self.kolvo_2 = 0
		
	def draw(self,screen):
		pygame.draw.rect(screen,(179,77,77),self.rect_2)
	
	def dell(st_2, kolvo_2, sp_disk_2):
		if kolvo_2 <= 0:
			kolvo_2 = 0
		else:
			kolvo_2 -= 1
			delete_2(sp_disk_2)
		return sp_disk_2
		
	def add(self, s, st_1, st_3, kolvo_1, kolvo_2, kovlo_3, sp_2):
		self.kolvo_2 += 1
		if s == 1:
			self.disk_2(self.b,st_1.kolvo_1 + 1,self.sp_disk_2, sp_2)
		elif s == 3:
			self.disk_2(self.b,st_3.kolvo_3 + 1,self.sp_disk_2, sp_2)
		elif s == 2:
			pass
		return self.sp_disk_2
		
	
class Sterzhni_3:
	def __init__(self,screen):
		self.razmer = 4, 405
		self.screen = screen
		left_3 = 563
		top = 15
		self.rect_3 = pygame.Rect((left_3,top),self.razmer)
		self.sp_disk_3 =[]
		self.c = 0
		self.kolvo_3 = 0
		
	def draw(self,screen):
		pygame.draw.rect(screen,(179,77,77),self.rect_3)
	
	def dell(st_3, kolvo_3, sp_disk_3):
		if kolvo_3 <= 0:
			kolvo_3 = 0
		else:
			kolvo_3 -= 1
			delete_3(sp_disk_3)
		return sp_disk_3
		
	def add(self, s, st_1, st_2, kolvo_1, kolvo_2, kovlo_3):
		self.kolvo_3 += 1
		if s == 1:
			self.disk_3(self.c,st_1.kolvo_1,self.sp_disk_3, sp)
		elif s == 2:
			st_3.disk_1(self.c,st_2.kolvo_2,self.sp_disk_3, sp)
		elif s == 3:
			pass
		return self.sp_disk_3
		

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
	
def draw(sp_disk, screen): 
	for disk in sp_disk:
		pygame.draw.rect(screen,(87,57,205),disk)
		
	
def ramka(screen, width, height, left, top):
	ramka = pygame.Rect((left,top),(width,height))
	pygame.draw.rect(screen,(0,255,0),ramka, 3)
			
def ramka2(screen, width, height, left, top):
	ramka = pygame.Rect((left,top),(width,height))
	pygame.draw.rect(screen,(255,0,0),ramka, 3)

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


def disk(s, st_1, st_2, st_3, kolvo_1, kolvo_2, kolvo_3, sp_disk_1, sp_disk_2, sp_disk_3):
	if s == 1:
		sp = preo(st_1.sp_disk_1, st_1.kolvo_1)
		st_1.dell(st_1, sp_disk_1)
		i = 0
		while i < kolvo:
			left = 15 + i*5
			i +=1
		top = 400 - a*21
		disk = pygame.Rect((left,top), sp)
		st_1.sp_disk_1.append(disk)
		st_1.a += 1
		return st_1.sp_disk_1
		
	if s == 2:
		sp = preo(st_2.sp_disk_2, st_2.kolvo_2)
		i = 0
		while i < kolvo:
			left = 245 + i*5
			i +=1
		top = 400 - b*21
		disk = pygame.Rect((left,top), sp)
		st_2.sp_disk_2.append(disk)
		st_2.b += 1
		return st_2.sp_disk_2
			
	if s == 3:
		sp = preo(st_3.sp_disk_3, st_3.kolvo_3)
		i = 0
		while i < kolvo:
			left = 475 + i*5
			i +=1
		top = 400 - c*21
		disk = pygame.Rect((left,top), sp)
		st_3.sp_disk_3.append(disk)
		st_3.c +=1
		return st_3.sp_disk_3
