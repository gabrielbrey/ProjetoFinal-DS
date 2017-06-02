import pygame
import time
import random

pygame.init()

white = (255,255,255)
black  = (0,0,0)
red = (175,0,0)
green = (0,155,0)

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
		
	if tela == tela3:
		pwidht1 = 30
		pheight1 = 50
		px1 = 0
		py1 = (display_height-25)/2
		pygame.draw.rect(gameDisplay,black,(px1,py1,pwidht1,pheight1))
		
		pwidht2 = 30
		pheight2 = 50
		px2 = display_width-pwidht2
		py2 = (display_height-25)/2
		pygame.draw.rect(gameDisplay,black,(px2,py2,pwidht2,pheight2))
	
	if tela == tela4:	
		pwidht1 = 50
		pheight1 = 50
		px1 = (display_width-25)/2
		py1 = display_height-pheight1
		
		pwidht2 = 34
		pheight2 = 50
		px2 = 0
		py2 = (display_height-25)/2
		
		pygame.draw.rect(gameDisplay,black,(px1,py1,pwidht1,pheight1))
		pygame.draw.rect(gameDisplay,black,(px2,py2,pwidht2,pheight2))
		
	if tela == tela5:
		pwidht1 = 50
		pheight1 = 50
		px1 = (display_width-25)/2
		py1 = 0
		
		pwidht2 = 60
		pheight2 = 50
		px2 = (display_width-30)/2
		py2 = display_height-50
		
		pygame.draw.rect(gameDisplay,black,(px1,py1,pwidht1,pheight1))
		pygame.draw.rect(gameDisplay,black,(px2,py2,pwidht2,pheight2))
		
	if tela == tela6:
		px1 = (display_width-30)/2
		py1 = 0
		pwidht1 = 60
		pheight1 = 50
			
		
		pygame.draw.rect(gameDisplay,black,(px1,py1,pwidht1,pheight1))
		
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
		lwidht = 200
		lheight = 240
		lx = (display_width-lwidht)/2
		ly = (display_height-lheight)/2
		
		
		pygame.draw.rect(gameDisplay,red,(lx,ly,lwidht,lheight))
		#COLISAO
		if lead_x>= lx and lead_x <= lx + lwidht or lead_x + block_size>= lx and lead_x + block_size <= lx + lwidht:
			if lead_y>= ly and lead_y <= ly + lheight or lead_y + block_size>= ly and lead_y + block_size <= ly + lheight:
				
				print ('colisao')
				return 1
	
	if tela == tela4:
		lx1 = 36
		ly1 = (display_height/2)+70
		lwidht1 = (display_width/2)-32
		lheight1 = 100
		pygame.draw.rect(gameDisplay,red,(lx1,ly1,lwidht1,lheight1))											
		if lead_x>= lx1 and lead_x <= lx1 + lwidht1 or lead_x + block_size>= lx1 and lead_x + block_size <= lx1 + lwidht1:
			if lead_y>= ly1 and lead_y <= ly1 + lheight1 or lead_y + block_size>= ly1 and lead_y + block_size <= ly1 + lheight1:
				return 1
				
		lx2 = display_width/2
		ly2 = 120
		lwidht2 = 60
		lheight2 = (display_width/2)-50
		pygame.draw.rect(gameDisplay,red,(lx2,ly2,lwidht2,lheight2))											
		if lead_x>= lx2 and lead_x <= lx2 + lwidht2 or lead_x + block_size>= lx2 and lead_x + block_size <= lx2 + lwidht2:
			if lead_y>= ly2 and lead_y <= ly2 + lheight2 or lead_y + block_size>= ly2 and lead_y + block_size <= ly2 + lheight2:
				return 1
	
	if tela == tela5:
		lx1 = 34
		ly1 = 50
		lwidht1 = 100
		lheight1 = 250
		pygame.draw.rect(gameDisplay,red,(lx1,ly1,lwidht1,lheight1))											
		if lead_x>= lx1 and lead_x <= lx1 + lwidht1 or lead_x + block_size>= lx1 and lead_x + block_size <= lx1 + lwidht1:
			if lead_y>= ly1 and lead_y <= ly1 + lheight1 or lead_y + block_size>= ly1 and lead_y + block_size <= ly1 + lheight1:
				return 1
		
		lwidht2 = 100
		lheight2 = 250
		lx2 = display_width-34-lwidht2
		ly2 = 50
		pygame.draw.rect(gameDisplay,red,(lx2,ly2,lwidht2,lheight2))											
		if lead_x>= lx2 and lead_x <= lx2 + lwidht2 or lead_x + block_size>= lx2 and lead_x + block_size <= lx2 + lwidht2:
			if lead_y>= ly2 and lead_y <= ly2 + lheight2 or lead_y + block_size>= ly2 and lead_y + block_size <= ly2 + lheight2:
				return 1
		
		lwidht3 = 250
		lheight3 = 70
		lx3 = display_width-34-lwidht3
		ly3 = 300
		pygame.draw.rect(gameDisplay,red,(lx3,ly3,lwidht3,lheight3))											
		if lead_x>= lx3 and lead_x <= lx3 + lwidht3 or lead_x + block_size>= lx3 and lead_x + block_size <= lx3 + lwidht3:
			if lead_y>= ly3 and lead_y <= ly3 + lheight3 or lead_y + block_size>= ly3 and lead_y + block_size <= ly3 + lheight3:
				return 1	
					
		lwidht4 = 250
		lheight4 = 70
		lx4 = 34
		ly4 = 300
		pygame.draw.rect(gameDisplay,red,(lx4,ly4,lwidht4,lheight4))											
		if lead_x>= lx4 and lead_x <= lx4 + lwidht4 or lead_x + block_size>= lx4 and lead_x + block_size <= lx4 + lwidht4:
			if lead_y>= ly4 and lead_y <= ly4 + lheight4 or lead_y + block_size>= ly4 and lead_y + block_size <= ly4 + lheight4:
				return 1	
				
		lwidht5 = 100
		lheight5 = 20
		lx5 = (display_width/2)-(lwidht5/2)
		ly5 = 450
		pygame.draw.rect(gameDisplay,red,(lx5,ly5,lwidht5,lheight5))											
		if lead_x>= lx5 and lead_x <= lx5 + lwidht5 or lead_x + block_size>= lx5 and lead_x + block_size <= lx5 + lwidht5:
			if lead_y>= ly5 and lead_y <= ly5 + lheight5 or lead_y + block_size>= ly5 and lead_y + block_size <= ly5 + lheight5:
				return 1
				
	if tela == tela6:
		lwidht1 = display_width-200
		lheight1 =30
		lx1 = 34
		ly1 = 130
		pygame.draw.rect(gameDisplay,red,(lx1,ly1,lwidht1,lheight1))											
		if lead_x>= lx1 and lead_x <= lx1 + lwidht1 or lead_x + block_size>= lx1 and lead_x + block_size <= lx1 + lwidht1:
			if lead_y>= ly1 and lead_y <= ly1 + lheight1 or lead_y + block_size>= ly1 and lead_y + block_size <= ly1 + lheight1:
				#return 1
				pass
		
		ly2 = 250
		lwidht2 = 30
		lheight2 = display_height-ly2-44
		lx2 = lx1+lwidht1-lwidht2
		pygame.draw.rect(gameDisplay,red,(lx2,ly2,lwidht2,lheight2))											
		if lead_x>= lx2 and lead_x <= lx2 + lwidht2 or lead_x + block_size>= lx2 and lead_x + block_size <= lx2 + lwidht2:
			if lead_y>= ly2 and lead_y <= ly2 + lheight2 or lead_y + block_size>= ly2 and lead_y + block_size <= ly2 + lheight2:
				return 1
				
def inimigo1 (lead_x,lead_y,direction):
	global gameEnd
	global vivo1
	global vivo2
	global vivo3
	global vivo4
	global vivo5
	global vivo6
	global vivo7
	global vivo8
	global vivo9
	
	if tela == tela2:
		yar = 50
		war = 60
		har = 30
		xar = display_width/2
		yar2 = 51
		xar2 = 300
		yar2 = 50
		
		##ARANhA 1
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
			if lead_y >= yar2 or lead_y <= yar2+har:
				if lead_x+50 >= xar2	:
					print("morreu i guess")
					vivo2= False			
		if direction == 'lefta' :					
			if lead_y >= yar2 or lead_y <= yar2+har:
				if lead_x+50 >= xar2	:
					print("morreu i guess")
					vivo2= False		
		if vivo2 == True:
			gameDisplay.blit(aranha,(xar2, yar2))#colisao
			if lead_x>= xar2 and lead_x <= xar2 + war or lead_x + block_size>= xar2 and lead_x + block_size <= xar2 + war:
				if lead_y>= yar2 and lead_y <= yar2 + har or lead_y + block_size>= yar2 and lead_y + block_size <= yar2 + har:
					print ('colisao2')
					return 1 
		
	if tela == tela3:
		xz = display_width/2
		yz = (display_height)-90
		hz = 30
		wz = 30
		
		##zumbi 1
		if direction == 'righta':	#COMBATE
			if lead_y >= yz and lead_y <= yz+hz:
				if lead_x+50 >= xz:
					print("morreu i guess")
					vivo3= False			
		if direction == 'lefta' :					
			if lead_y >= yz and lead_y <= yz+hz:
				if lead_x+50 >= xz	:
					print("morreu i guess")
					vivo3= False	
					
		if vivo3 == True:
			gameDisplay.blit(zumbi,(xz, yz))#colisao
			if lead_x>= xz and lead_x <= xz + wz or lead_x + block_size>= xz and lead_x + block_size <= xz + wz:
				if lead_y>= yz and lead_y <= yz + hz or lead_y + block_size>= yz and lead_y + block_size <= yz + hz:
					print ('colisao')
					return 1	
		
		yar = 50
		war = 60
		har = 30
		xar = display_width/2
		
		##ARANHA 1
		if direction == 'righta':	#COMBATE
			if lead_y >= yar or lead_y <= yar+har:
				if lead_x+50 >= xar	:
					print("morreu i guess")
					vivo4= False			
		if direction == 'lefta' :					
			if lead_y >= yar or lead_y <= yar+har:
				if lead_x+50 >= xar	:
					print("morreu i guess")
					vivo4= False		
		if vivo4 == True:
			gameDisplay.blit(aranha,(xar, yar))#colisao
			if lead_x>= xar and lead_x <= xar + war or lead_x + block_size>= xar and lead_x + block_size <= xar + war:
				if lead_y>= yar and lead_y <= yar + har or lead_y + block_size>= yar and lead_y + block_size <= yar + har:
					print ('colisao2')
					return 1 
		
	if tela == tela4:
		yar = display_height/2
		war = 60
		har = 30
		xar = 470
		
		##ARANHA 1
		if direction == 'righta':	#COMBATE
			if lead_y >= yar or lead_y <= yar+har:
				if lead_x+50 >= xar	:
					print("morreu i guess")
					vivo5= False			
		if direction == 'lefta' :					
			if lead_y >= yar or lead_y <= yar+har:
				if lead_x+50 >= xar	:
					print("morreu i guess")
					vivo5= False		
		if vivo5 == True:
			gameDisplay.blit(aranha,(xar, yar))#colisao
			if lead_x>= xar and lead_x <= xar + war or lead_x + block_size>= xar and lead_x + block_size <= xar + war:
				if lead_y>= yar and lead_y <= yar + har or lead_y + block_size>= yar and lead_y + block_size <= yar + har:
					print ('colisao2')
					return 1

		hz = 30
		wz = 60
		xz = display_width-wz-34
		yz = (display_height)-170
		##zumbi 1
		if direction == 'righta':	#COMBATE
			if lead_y >= yz and lead_y <= yz+hz:
				if lead_x+50 >= xz:
					print("morreu i guess")
					vivo8= False			
		if direction == 'lefta' :					
			if lead_y >= yz and lead_y <= yz+hz:
				if lead_x+50 >= xz	:
					print("morreu i guess")
					vivo8= False	
					
		if vivo8 == True:
			gameDisplay.blit(aranha,(xz, yz))#colisao
			if lead_x>= xz and lead_x <= xz + wz or lead_x + block_size>= xz and lead_x + block_size <= xz + wz:
				if lead_y>= yz and lead_y <= yz + hz or lead_y + block_size>= yz and lead_y + block_size <= yz + hz:
					print ('colisao')
					return 1	

	if tela == tela5:	
		xz = display_width-200
		yz = 500
		hz = 30
		wz = 30
		##esqueleto1
		if direction == 'righta':	#COMBATE
			if lead_y >= yz and lead_y <= yz+hz:
				if lead_x+50 >= xz:
					print("morreu i guess")
					vivo6= False			
		if direction == 'lefta' :					
			if lead_y >= yz and lead_y <= yz+hz:
				if lead_x-50 >= xz	:
					print("morreu i guess")
					vivo6= False	
					
		if vivo6 == True:
			gameDisplay.blit(esqueleto,(xz, yz))#colisao
			if lead_x>= xz and lead_x <= xz + wz or lead_x + block_size>= xz and lead_x + block_size <= xz + wz:
				if lead_y>= yz and lead_y <= yz + hz or lead_y + block_size>= yz and lead_y + block_size <= yz + hz:
					print ('colisao')
					return 1	
		
		yar = 500
		war = 30
		har = 30
		xar = 200
		##esqueleto2
		if direction == 'righta':	#COMBATE
			if lead_y >= yar and lead_y <= yar+har:
				if lead_x+50 >= xar	:
					print("morreu i guess")
					vivo7= False			
		if direction == 'lefta' :					
			if lead_y >= yar and lead_y <= yar+har:
				if lead_x-50 >= xar	:
					print("morreu i guess")
					vivo7= False		
		if vivo7 == True:
			gameDisplay.blit(esqueleto,(xar, yar))#colisao
			if lead_x>= xar and lead_x <= xar + war or lead_x + block_size>= xar and lead_x + block_size <= xar + war:
				if lead_y>= yar and lead_y <= yar + har or lead_y + block_size>= yar and lead_y + block_size <= yar + har:
					print ('colisao2')
					return 1 
					
	if tela == tela6:
		xz = 200
		yz = display_height/2
		hz = 50
		wz = 50
		##demonho
		if direction == 'righta':	#COMBATE
			if lead_y >= yz and lead_y <= yz+hz:
				if lead_x+50 >= xz:
					print("morreu i guess")
					vivo9= False
					gameEnd = True
		if direction == 'lefta' :					
			if lead_y >= yz and lead_y <= yz+hz:
				if lead_x+50 >= xz	:
					print("morreu i guess")
					vivo9= False
					gameEnd = True
					
		if vivo9 == True:
			gameDisplay.blit(demonho,(xz, yz))#colisao
			if lead_x>= xz and lead_x <= xz + wz or lead_x + block_size>= xz and lead_x + block_size <= xz + wz:
				if lead_y>= yz and lead_y <= yz + hz or lead_y + block_size>= yz and lead_y + block_size <= yz + hz:
					print ('colisao')
					return 1	
		
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

	
	txtSurf , txtRect = text_objetcs(msg , color,size)
	txtRect.center = int(display_width/2 ),int((display_height/2)+y_displace)
	gameDisplay.blit(txtSurf , txtRect)
	
def button(img,x,y,widht,height,img2,action = None):
	global paused
	global tela
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()	
		
	if x+widht > cur[0] > x and y+height > cur[1] >y:
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
zumbi = pygame.image.load('zumbi3030.png')
goimg = pygame.image.load('gover.png')
esqueleto = pygame.image.load('esqueleto3030.png')
demonho = pygame.image.load('devil.png')
fim = pygame.image.load('fim.png')

tela = telainicio
appleThickness = 30
clock = pygame.time.Clock()

def gameLoop():
	global gameEnd
	global direction
	global tela
	global vivo1
	global vivo2
	global vivo3
	global vivo4
	global vivo5
	global vivo6
	global vivo7
	global vivo8
	global vivo9
	
	vivo1 = True
	vivo2 = True
	vivo3 = True
	vivo4 = True
	vivo5 = True
	vivo6 = True
	vivo7 = True
	vivo8 = True
	vivo9 = True
	
	
	direction = 'right'
	gameExit = False
	gameOver = False
	gameEnd = False

	lead_x = 61  
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0
	movx = 20
	movy = 20
	
	posi = []
	inipos = []
	snakeLenght = 1
	
	while not gameExit:   
		while gameEnd == True: 
			gameDisplay.blit(fim , [0,(display_height/2)-100]
			button(bco2,50,500,200,50,bco1,action = "menu")
			button(bsa1,650,500,100,50,bsa2,action = "quit")
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:	
					gameExit = True
					gameOver = False
			
			pygame.display.update()
		
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
			px = (display_width-30)/2
			py = 0
			pwidht = 60
			pheight = 50
			
			if lead_x>= px and lead_x <= px + pwidht or lead_x + block_size>= px and lead_x + block_size <= px + pwidht:
				if lead_y>= py and lead_y <= py + pheight or lead_y + block_size>= py and lead_y + block_size <= py + pheight: 			#cima
					tela = tela2
					lead_y = display_height - (pheight+block_size+1)
						
			if lead_y > display_height-50 :	#paredes
				lead_y -= block_size
			if lead_x > display_width-50 :
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
					tela = tela3  #PORTA2
					lead_x = 50
			if lead_x>= px1 and lead_x <= px1 + pwidht1 or lead_x + block_size>= px and lead_x + block_size <= px1 + pwidht1:
				if lead_y>= py1 and lead_y <= py1 + pheight1 or lead_y+ block_size>= py1 and lead_y + block_size <= py1 + pheight1: 			#cima
					tela = telainicio #PORTA1
					lead_y = 60
	
			if lead_y > display_height-50 :	#paredes
				lead_y -= block_size
			if lead_x > display_width-50 :
				lead_x -= block_size
			if lead_x < 50 : 
				lead_x = block_size
			if lead_y < 49:  
				lead_y = block_size
		
		if tela == tela3:
			pwidht1 = 30
			pheight1 = 50
			pwidht2 = 30
			pheight2 = 50
			px1 = 0
			py1 = (display_height-25)/2
			px2 = display_width-pwidht2
			py2 = (display_height-25)/2
			
			if lead_x>= px1 and lead_x <= px1 + pwidht1 or lead_x + block_size>= px and lead_x + block_size <= px1 + pwidht1:
				if lead_y>= py1 and lead_y <= py1 + pheight1 or lead_y+ block_size>= py1 and lead_y + block_size <= py1 + pheight1: 			#cima
					tela = tela2 #PORTA1
					lead_x = display_width-80
			if lead_x>= px2 and lead_x <= px2 + pwidht2 or lead_x + block_size>= px2 and lead_x + block_size <= px2 + pwidht2:
				if lead_y>= py2 and lead_y <= py2 + pheight2 or lead_y + block_size>= py2 and lead_y + block_size <= py2 + pheight2: 			#cima
					tela = tela4 #PORTA2
					lead_x = 50
			
			if lead_y > display_height-50 :	#paredes
				lead_y -= block_size
			if lead_x > display_width-50 :
				lead_x -= block_size
			if lead_x < 50 : 
				lead_x = block_size
			if lead_y < 49:  
				lead_y = block_size
		
		if tela == tela4:
			pwidht1 = 50
			pheight1 = 50
			px1 = (display_width-25)/2
			py1 = display_height-pheight1
			
			pwidht2 = 30
			pheight2 = 50
			px2 = 0
			py2 = (display_height-25)/2
		
			if lead_x>= px2 and lead_x <= px2 + pwidht2 or lead_x + block_size>= px2 and lead_x + block_size <= px2 + pwidht2:
				if lead_y>= py2 and lead_y <= py2 + pheight2 or lead_y + block_size>= py2 and lead_y + block_size <= py2 + pheight2: 			#cima
					tela = tela3  #PORTA2
					lead_x = display_width-50
			if lead_x>= px1 and lead_x <= px1 + pwidht1 or lead_x + block_size>= px and lead_x + block_size <= px1 + pwidht1:
				if lead_y>= py1 and lead_y <= py1 + pheight1 or lead_y+ block_size>= py1 and lead_y + block_size <= py1 + pheight1: 			#cima
					tela = tela5#PORTA1
					lead_y = 60
	
			if lead_y > display_height-50 :	#paredes
				lead_y -= block_size
			if lead_x > display_width-50 :
				lead_x -= block_size
			if lead_x < 50 : 
				lead_x = block_size
			if lead_y < 49:  
				lead_y = block_size
			
		if tela == tela5:	
			pwidht1 = 50
			pheight1 = 50
			px1 = (display_width-25)/2
			py1 = 0
			
			pwidht2 = 60
			pheight2 = 50
			px2 = (display_width-30)/2
			py2 = display_height-50
		
			if lead_x>= px2 and lead_x <= px2 + pwidht2 or lead_x + block_size>= px2 and lead_x + block_size <= px2 + pwidht2:
				if lead_y>= py2 and lead_y <= py2 + pheight2 or lead_y + block_size>= py2 and lead_y + block_size <= py2 + pheight2: 			#cima
					tela = tela6  #PORTA2
					lead_y = 70
			if lead_x>= px1 and lead_x <= px1 + pwidht1 or lead_x + block_size>= px and lead_x + block_size <= px1 + pwidht1:
				if lead_y>= py1 and lead_y <= py1 + pheight1 or lead_y+ block_size>= py1 and lead_y + block_size <= py1 + pheight1: 			#cima
					tela = tela4#PORTA1
					lead_y = display_height-70
	
			if lead_y > display_height-50 :	#paredes
				lead_y -= block_size
			if lead_x > display_width-50 :
				lead_x -= block_size
			if lead_x < 50 : 
				lead_x = block_size
			if lead_y < 49:  
				lead_y = block_size
				
		if tela == tela6:
		
			px = (display_width-30)/2
			py = 0
			pwidht = 60
			pheight = 50
			
			if lead_x>= px and lead_x <= px + pwidht or lead_x + block_size>= px and lead_x + block_size <= px + pwidht:
				if lead_y>= py and lead_y <= py + pheight or lead_y + block_size>= py and lead_y + block_size <= py + pheight: 			#cima
					tela = tela5
					lead_y = display_height - (pheight+block_size+1)
			
			if lead_y > display_height-50 :	#paredes
				lead_y -= block_size
			if lead_x > display_width-50 :
				lead_x -= block_size
			if lead_x < 50 : 
				lead_x = block_size
			if lead_y < 49:  
				lead_y = block_size

		
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