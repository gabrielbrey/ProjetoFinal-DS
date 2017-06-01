import pygame
import time
import random

pygame.init()

white = (255,255,255)
black  = (0,0,0)
red = (200,0,0)
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

def porta(lead_x,lead_y):
	if tela == telainicio:
		px1 = (display_width-30)/2
		py1 = 0
		pwidht1 = 60
		pheight1 = 50
		
		pygame.draw.rect(gameDisplay,black,(px1,py1,pwidht1,pheight1))
				
	if tela == tela2:	
		pwidht1 = 50
		pheight1 = 50
		px1 = (display_width-25)/2
		py1 = display_height-pheight1
		
		pwidht2 = 30
		pheight2 = 50
		px2 = display_width-pwidht2
		py2 = (display_height-25)/2
		
		pygame.draw.rect(gameDisplay,black,(px1,py1,pwidht1,pheight1))
		pygame.draw.rect(gameDisplay,black,(px2,py2,pwidht2,pheight2))
		
def lava(lead_x,lead_y):
				
	if tela == tela2:
		lx1 = display_width/2
		ly1 = (display_height/2)+50
		lwidht1 = (display_width/2)-32
		lheight1 = 100
		pygame.draw.rect(gameDisplay,red,(lx1,ly1,lwidht1,lheight1))											
		if lead_x>= lx1 and lead_x <= lx1 + lwidht1 or lead_x + block_size>= lx1 and lead_x + block_size <= lx1 + lwidht1:
			if lead_y>= ly1 and lead_y <= ly1 + lheight1 or lead_y + block_size>= ly1 and lead_y + block_size <= ly1 + lheight1:
				return 1
				
		lx2 = display_width/2
		ly2 = 100
		lwidht2 = 30
		lheight2 = (display_width/2)-50
		pygame.draw.rect(gameDisplay,red,(lx2,ly2,lwidht2,lheight2))											
		if lead_x>= lx2 and lead_x <= lx2 + lwidht2 or lead_x + block_size>= lx2 and lead_x + block_size <= lx2 + lwidht2:
			if lead_y>= ly2 and lead_y <= ly2 + lheight2 or lead_y + block_size>= ly2 and lead_y + block_size <= ly2 + lheight2:
				return 1
				
	if tela == tela3:
		lx = display_width/2
		ly = display_height/2
		lwidht = 20
		lheight = 30
		
		pygame.draw.rect(gameDisplay,red,(lx,ly,lwidht,lheight))
		#COLISAO
		if lead_x>= lx and lead_x <= lx + lwidht or lead_x + block_size>= lx and lead_x + block_size <= lx + lwidht:
			if lead_y>= ly and lead_y <= ly + lheight or lead_y + block_size>= ly and lead_y + block_size <= ly + lheight:
				
				print ('colisao')
				return 1
	
def inimigo1 (lead_x,lead_y,direction):
	#xar = display_width/2
	global vivo1
	global vivo2
	
	if tela == tela2:
		yar = 50
		war = 60
		har = 30
		xar = display_width/2
		xar2 = 300
		
		##ARANA 1
		if direction == 'righta':	#COMBATE
			if lead_y >= yar or lead_y <= yar+har:
				if lead_x+50 >= xar:
					print("morreu i guess")
					vivo1= False			
		if direction == 'lefta' :					
			if lead_y >= yar or lead_y <= yar+har:
				if lead_x+50 >= xar	:
					print("morreu i guess")
					vivo1= False	
					
		if vivo1 == True:
			gameDisplay.blit(aranha,(xar, yar))#colisao
			if lead_x>= xar and lead_x <= xar + war or lead_x + block_size>= xar and lead_x + block_size <= xar + war:
				if lead_y>= yar and lead_y <= yar + har or lead_y + block_size>= yar and lead_y + block_size <= yar + har:
					print ('colisao')
					return 1	
		##ARANHA 2
		if direction == 'righta':	#COMBATE
			if lead_y >= yar or lead_y <= yar+har:
				if lead_x+50 >= xar2	:
					print("morreu i guess")
					vivo2= False			
		if direction == 'lefta' :					
			if lead_y >= yar or lead_y <= yar+har:
				if lead_x+50 >= xar2	:
					print("morreu i guess")
					vivo2= False		
		if vivo2 == True:
			gameDisplay.blit(aranha,(xar2, yar))#colisao
			if lead_x>= xar2 and lead_x <= xar2 + war or lead_x + block_size>= xar and lead_x + block_size <= xar2 + war:
				if lead_y>= yar and lead_y <= yar + har or lead_y + block_size>= yar and lead_y + block_size <= yar + har:
					print ('colisao2')
					return 1 
		
	
			##colocar +1 em uma lista de pontos
def pause():
	global paused
	paused = True
	gameDisplay.blit(pausaimg,[0, (display_height/2)-0])
	#message_to_screen("C para continuar Q para sair" , white , 175)
	gameDisplay.blit(logoimg,[0, (display_height/2)-150])
	pygame.display.update()
	#clock.tick(5)			
	while paused:
		button(bco2,150,500,200,50,bco1,action = "cont")
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
			
		telas(tela)	
		gameDisplay.blit(logoimg , [0, logoy])
		
		#message_to_screen("Dungeon Runners",red,-100,"large")
		gameDisplay.blit(instruimg , [0,(display_height/2)])
		
		button(bjo1,150,500,120,50,bjo2,action = "play")
		button(bsc1,290,500,250,50,bsc2,action = "score")
		button(bsa1,550,500,100,50,bsa2,action = "quit")
	
		pygame.display.update()
		clock.tick(10)	

def score(score):
	text = smallfont.render("Score: " + str(score),True , white)
	gameDisplay.blit(text,[0,0])
		
def player (posi,block_size):
	if direction == "right":
		head = imgr
	if direction == "left":
		head = imgl
	if direction == "lefta":
		head = imgra
		
	if direction == "righta":
		head = imgla
		

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
	global paused
	global tela
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()	
		
	if x+widht > cur[0] > x and y+height > cur[1] >y:
		#pygame.draw.rect(gameDisplay,color2,(x,y,widht,height))
		gameDisplay.blit(img , (x,y))
		if click[0] == 1 and action != None:
			
			if action == "play":
				gameLoop()
				
			elif action == "quit":
				pygame.quit()
				quit()
				
			elif action == "score":
				print("not yet m8")
			
			elif action == "cont":
				paused = False
				
			elif action == "menu":
				tela = telainicio
				pygame.time.wait(200)
				game_intro()
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
imgra = pygame.image.load('knightal.png')
imgla =  pygame.image.load('knightar.png')
logoimg = pygame.image.load('logo.png')
telainicio = pygame.image.load('room.png')
tela2 = pygame.image.load('r2.png')
tela3 = pygame.image.load('r3.png')
tela4 = pygame.image.load('r4.png')
tela5 = pygame.image.load('r5.png')
tela6 = pygame.image.load('r6.png')
bjo1 = pygame.image.load('bjo1.png')
bjo2 = pygame.image.load('bjo2.png')
bsc1 =  pygame.image.load('bsc1.png')
bsc2 =  pygame.image.load('bsc2.png')
bsa1 =  pygame.image.load('bsa1.png')
bsa2 =  pygame.image.load('bsa2.png')
pausaimg = pygame.image.load('bpa1.png')
bco1 = pygame.image.load('bco1.png')
bco2 = pygame.image.load('bco2.png')
portaimg = pygame.image.load('porta.png')
instruimg = pygame.image.load('instru.png')
aranha = pygame.image.load('aranha6030.png')
goimg = pygame.image.load('gover.png')

tela = telainicio
appleThickness = 30
clock = pygame.time.Clock()

def gameLoop():
	global direction
	global tela
	global vivo1
	global vivo2
	
	vivo1 = True
	vivo2 = True	
	
	appleThickness = 30
	
	
	direction = 'right'
	gameExit = False
	gameOver = False

	lead_x = 61  #display_width/2
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0
	movx = 20
	movy = 20
	
	posi = []
	inipos = []
	snakeLenght = 1
	
	while not gameExit:   
	
		while gameOver == True: 
			gameDisplay.fill(black)
			gameDisplay.blit(goimg , [0,(display_height/2)-100])
			button(bco2,50,500,200,50,bco1,action = "menu")
			button(bsa1,650,500,100,50,bsa2,action = "quit")
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:	
					gameExit = True
					gameOver = False
			
			pygame.display.update()

		for event in pygame.event.get(): 
			#print(event)
			if event.type == pygame.QUIT:
				gameExit = True 
			
			if event.type == pygame.KEYDOWN:
					
				if event.key == pygame.K_a:
					direction = "left"
					lead_x_change = -movx
					lead_y_change = 0
				elif event.key == pygame.K_d:
					direction = "right"
					lead_x_change = movx
					lead_y_change = 0
				elif event.key == pygame.K_w:
					#direction = "up"
					lead_y_change = -movy
					lead_x_change = 0
				elif event.key == pygame.K_s:
					#direction = "down"
					lead_y_change = movy
					lead_x_change = 0
				
				elif event.key == pygame.K_p:
					pause()
			
			elif event.type == pygame.KEYUP:	
				if event.key == pygame.K_a or event.key == pygame.K_d:
					lead_x_change = 0
				elif event.key == pygame.K_w or event.key == pygame.K_s :
					#direction = "up"
					lead_y_change = 0
			
			if direction == "left":
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						print("ataquel")
						direction = "lefta"
						
						print("dpsataquel")
						
			if direction == "right":
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						print("ataquer")
						direction = "righta"

						print("dpsataquer")
						
		if tela == telainicio:	
			#pygame.draw.rect(gameDisplay,black,(((display_width/2)+20) ,0,40,10))
			##porta(lead_x,lead_y,)
			px = (display_width-30)/2
			py = 0
			pwidht = 60
			pheight = 50
			
			if lead_x>= px and lead_x <= px + pwidht or lead_x + block_size>= px and lead_x + block_size <= px + pwidht:
				if lead_y>= py and lead_y <= py + pheight or lead_y + block_size>= py and lead_y + block_size <= py + pheight: 			#cima
					tela = tela2
					lead_y = display_height - (pheight+block_size+1)
						
			if lead_y > display_height-50 :
				lead_y -= block_size
			if lead_x > display_width-50 :#or lead_x < display_width+50:	
				lead_x -= block_size
			if lead_x < 50 : 
				lead_x = block_size
			if lead_y < 49:  
				lead_y = block_size
		
		if tela == tela2:
			pwidht1 = 50
			pheight1 = 50
			px1 = (display_width-25)/2
			py1 = display_height-pheight1
			
			pwidht2 = 30
			pheight2 = 50
			px2 = display_width-pwidht2
			py2 = (display_height-25)/2
		
			if lead_x>= px2 and lead_x <= px2 + pwidht2 or lead_x + block_size>= px2 and lead_x + block_size <= px2 + pwidht2:
				if lead_y>= py2 and lead_y <= py2 + pheight2 or lead_y + block_size>= py2 and lead_y + block_size <= py2 + pheight2: 			#cima
					tela = tela3
					lead_x = 0+pwidht2+1
		
			if lead_x>= px1 and lead_x <= px1 + pwidht1 or lead_x + block_size>= px and lead_x + block_size <= px1 + pwidht1:
				if lead_y>= py1 and lead_y <= py1 + pheight1 or lead_y+ block_size>= py1 and lead_y + block_size <= py1 + pheight1: 			#cima
					tela = telainicio
					lead_y = 60
					
			if direction == "lefta":
				#if lead_x - 15 =< : 			#cima
					
				print("Ata")
			
					
			if lead_y > display_height-50 :
				lead_y -= block_size
			if lead_x > display_width-50 :#or lead_x < display_width+50:	
				lead_x -= block_size
			if lead_x < 50 : 
				lead_x = block_size
			if lead_y < 49:  
				lead_y = block_size
		
		if tela == tela3:
			if lead_x >= display_width:		#direita
				tela = tela4
				lead_x = 0+5
			elif  lead_x < 0 :				#Esquerda
				tela = tela2
				lead_x = display_width+5
			
			#gameDisplay.blit(img())
			
			if lead_y < 50:  
				lead_y = block_size
			if lead_y >display_height-50 : 
				lead_y -= block_size
		
		if tela == tela4:
			if lead_y >= display_height : #baixo
				tela = tela5 
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
					
		porta(lead_x,lead_y)
		
		player(posi,block_size)
		
		inimigo1(lead_x,lead_y,direction)
		
		lava(lead_x,lead_y)				#########ihfaofoivbajiscbvjoibfdhjk\vh9esoifjbueikillmeplz
		if lava(lead_x,lead_y) == 1 or inimigo1(lead_x,lead_y,direction) == 1 :
			gameOver = True 
		else:
			pass
		
		pygame.display.update()
		
		clock.tick(FPS)
		
	pygame.quit()
	quit()
	
game_intro()

gameLoop()