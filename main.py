import pygame
import time
import random

pygame.init()

white = (255,255,255)
black  = (0,0,0)
red = (255,0,0)
green = (0,155,0)
trans = (255,255,255,128)

display_width = 800
display_height = 600

block_size = 30

FPS = 20

direction = "right"

smallfont = pygame.font.SysFont("arialms  ",25)
medfont = pygame.font.SysFont("arialms  ",50)
largefont = pygame.font.SysFont("arialms  ",80)

# def randAppleGen():
	# randAppleX = round(random.randrange(0,display_width-appleThickness))#/10.0)*10	
	# randAppleY = round(random.randrange(0, display_height-appleThickness))#/10.0)*10
	# return randAppleX , randAppleY

def pause():
	paused = True
	
	gameDisplay.blit(pausaimg,[0, (display_height/2)-0])
	#message_to_screen("C para continuar Q para sair" , white , 175)
	
	gameDisplay.blit(logoimg,[0, (display_height/2)-150])
	
	pygame.display.update()
	#clock.tick(5)		
	
	while paused:
	
		button(bco2,150,500,200,50,bco1,action = "cont")##ARRUMAR
		button(bsa1,550,500,100,50,bsa2,action = "quit")
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()		
		
		pygame.display.update()
	
def telas (tela):
	gameDisplay.blit(tela , [0,0])
	
def game_intro():
	pygame.mixer.music.load('muint.mp3')
	logoy = (display_height/2)-150
	
	intro = True
	if intro:
		pygame.mixer.music.play(-1)
	while intro :
		
		
		for event in pygame.event.get():	
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				
		telas(tela)	
		gameDisplay.blit(logoimg , [0, logoy])
		
		#gameDisplay.fill(black)
		
		#message_to_screen("Dungeon Runners",red,-100,"large")
		message_to_screen("Use WASD para se mover",white,-30)
		message_to_screen("Pressione P para Pausar o jogo",white,0)
		
		button(bjo1,150,500,120,50,bjo2,action = "play")
		button(bsc1,290,500,250,50,bsc2,action = "score")
		button(bsa1,550,500,100,50,bsa2,action = "quit")
	
		pygame.display.update()
		clock.tick(5)		
	

def score(score):
	text = smallfont.render("Score: " + str(score),True , white)
	gameDisplay.blit(text,[0,0])
		
def player (posi,block_size):
	if direction == "right":
		head = imgr
	if direction == "left":
		head = imgl
	#if direction == "up":
	#	head = imgr
	#if direction == "down":
	#	head = imgl

	gameDisplay.blit(head,(posi[-1][0], posi[-1][1]))

def text_objetcs (text , color,size):
	if size == 'small':
		txtSurf = smallfont.render(text , True , color)
	elif size == 'medium':
		txtSurf = medfont.render(text , True , color)
	elif size == 'large':
		txtSurf = largefont.render(text , True , color)
	return txtSurf , txtSurf.get_rect()	
	
def text_to_button (msg,color,buttonx,buttony,buttonwidth,buttonheight,size = "small" ):
	txtSurf , txtRect = text_objetcs(msg,color,size)
	txtRect.center = ((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
	gameDisplay.blit(txtSurf , txtRect)
	
def message_to_screen (msg,color,y_displace=0,size = "small"):
	
	txtSurf , txtRect = text_objetcs(msg , color,size)
	txtRect.center = int(display_width/2 ),int((display_height/2)+y_displace)
	gameDisplay.blit(txtSurf , txtRect)

def button(img,x,y,widht,height,img2,action = None):
	
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()	
		
	if x+widht > cur[0] > x and y+height > cur[1] >y:
		#pygame.draw.rect(gameDisplay,color2,(x,y,widht,height))
		gameDisplay.blit(img , (x,y))
		if click[0] == 1 and action != None:
			if action == "quit":
				pygame.quit()
				quit()
				
			if action == "play":
				gameLoop()
				
			if action == "score":
				print("not yet m8")
			
			if action == "cont":
				paused = False
		
	else:
		gameDisplay.blit(img2 , (x,y))
		
	#text_to_button(text,black,x,y,widht,height)
	
		
	
	
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Dungeon Runners")
icon = pygame.image.load('knightr.png')
pygame.display.set_icon(icon)
pygame.display.update()

imgl = pygame.image.load('knightr.png')
imgr = pygame.image.load('knightl.png')
logoimg =pygame.image.load('logo.png')
telainicio = pygame.image.load('room.png')
tela2 = pygame.image.load('r2.png')
tela3 = pygame.image.load('r3.png')
tela4 = pygame.image.load('r4.png')
tela5 = pygame.image.load('r5.png')
tela6 = pygame.image.load('r6.png')#
bjo1 = pygame.image.load('bjo1.png')
bjo2 = pygame.image.load('bjo2.png')
bsc1 =  pygame.image.load('bsc1.png')
bsc2 =  pygame.image.load('bsc2.png')
bsa1 =  pygame.image.load('bsa1.png')
bsa2 =  pygame.image.load('bsa2.png')
pausaimg = pygame.image.load('bpa1.png')
bco1 = pygame.image.load('bco1.png')
bco2 = pygame.image.load('bco2.png')


tela = telainicio
appleThickness = 30
clock = pygame.time.Clock()

def gameLoop():
	global direction
	global tela
	
	appleThickness = 30
	
	direction = 'right'
	gameExit = False
	gameOver = False

	lead_x = 0  #display_width/2
	lead_y = display_height/2
	lead_x_change = 10
	lead_y_change = 0
	
	posi = []
	snakeLenght = 1
	

	
	while not gameExit:
	
		while gameOver == True: #olocar as musica
			gameDisplay.fill(black)
			message_to_screen("GAME OVER",red,size = 'large')
			message_to_screen("C para continuar ou Q para sair",white, -50,size = 'medium')
			
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:	
					gameExit = True
					gameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key  == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key  == pygame.K_c:
						gameLoop()
			
			pygame.display.update()

		for event in pygame.event.get(): #colocar as musica
			#print(event)
			if event.type == pygame.QUIT:
				gameExit = True 
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					direction = "left"
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_d:
					direction = "right"
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_w:
					#direction = "up"
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_s:
					#direction = "down"
					lead_y_change = block_size
					lead_x_change = 0
				
				elif event.key == pygame.K_p:
					pause()
			
			elif event.type == pygame.KEYUP:	
				if event.key == pygame.K_a or event.key == pygame.K_d:
					lead_x_change = 0
				elif event.key == pygame.K_w or event.key == pygame.K_s :
					#direction = "up"
					lead_y_change = 0
				
		if tela == telainicio:	
			pygame.draw.rect(gameDisplay,black,(((display_width/2)+20) ,0,40,10))
			
			if lead_y < 0 and (display_width/2)+20 > lead_x > (display_width/2)-20 :   			#cima
				tela = tela2
				lead_y = display_height-5
			#lead_y < 0 and 
		
		if tela == tela2:
			
			if lead_x >= display_width:		#direita
				tela = tela3
				lead_x = 0+5		
			elif lead_y >= display_height : #baixo
				tela = telainicio 
				lead_y = 0+5			

		if tela == tela3:
			if lead_x >= display_width:		#direita
				tela = tela4
				lead_x = 0+5
			elif  lead_x < 0 :				#Esquerda
				tela = tela2
				lead_x = display_width+5
		
		if tela == tela4:		
			if lead_y >= display_height : #baixo
				tela = tela5 #barreirana1
				lead_y = 0+5	
			elif  lead_x < 0 :				#Esquerda
				tela = tela3
				lead_x = display_width+5
			
		if tela == tela5:	
			if  lead_x < 0 :				#Esquerda
				tela = tela6
				lead_x = display_width+5		
			elif lead_y < 0 :   			#cima
				tela = tela4
				lead_y = display_height-5
				
		lead_x += lead_x_change	
		lead_y += lead_y_change	
		
		gameDisplay.fill(black)	
		
		telas(tela)
	
		listaposi = []
		listaposi.append(lead_x)
		listaposi.append(lead_y)
		posi.append(listaposi)
		
		if len(posi)> snakeLenght:
			del posi[0]
		
			
		player(posi,block_size)
		
		
		pygame.display.update()
		
				
		clock.tick(FPS)
		
	pygame.quit()
	quit()
	
game_intro()

gameLoop()