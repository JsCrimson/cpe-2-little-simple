#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import pygame
import time

import random
from pygame. locals import *
import xlrd
import csv

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('my vocab')

FPS = 45


aaa = (0,255,255) #blue like a sky
bbb = (128,255,255) # soft of aaa
bff = (191,255,255) # sofer of bbb
cc = (128,145,195)
pink = (255,200,200)
edpink = (255,148,190)
papayawhip = (255,239,213)
white = (255,255,255)
wh = (245,128,120)
bla = (0,0,0)
liam = (0,255,128)
CRIMSON = (145,0,0)
darkblue = (0,0,128)
Mistryrose = (255,228,225)
dt = (0,206,209)
pvr = (219,112,147)
dodgerblue = (30,144,255)
pt = (175,238,238)
stblue = (70,200,155)
stbluer = (120,255,180)
salmon = (250,128,114)
bff = (191,255,255)
greensoft = (178,255,221)

clock = pygame.time.Clock()

cubcake = pygame.image.load('im/10.png')
jelly = pygame.image.load('im/8.png') 
floor = pygame.image.load('im/9.png')
princess = pygame.image.load('im/6.png')
candy = pygame.image.load('im/2.png')
banana = pygame.image.load('im/3.png')
snail = pygame.image.load('im/11.gif')
fin = pygame.image.load('im/22.gif')

cl = pygame.mixer.Sound("sound/click.mp3")
back = pygame.mixer.Sound("sound/back.wav")
correct = pygame.mixer.Sound("sound/correct.wav")
incorrect = pygame.mixer.Sound("sound/incorrect.wav")
time = pygame.mixer.Sound("sound/time.wav")
gamefail = pygame.mixer.Sound("sound/game-fail.wav")
nyancat = pygame.mixer.Sound("sound/NyanCat.mp3")
hello = pygame.mixer.Sound("sound/OMFG - Hello.mp3")


def game_intro():
   intro = True
   while intro :
      for event in pygame.event.get():
         if event.type == pygame.QUIT :
            pygame.quit()
            quit()

      screen.fill(Mistryrose)
      message_to_screen("V O C A B U L A R Y")
      mes("K A S E T S A R T  U N I V E R S I T Y")
      screen.blit(floor,(70,420))
      screen.blit(banana,(920,230))
      buttonintro ("QUIT",475,600,250,80,cc,stbluer,qq)
      buttonintro ("PLAY",475,500,250,80,wh,stbluer,playgame)
      buttonintro ("VOCAB",475,400,250,80,stblue,stbluer,see)
  

      pygame.display.update()
      clock.tick(30)

def show_score() :
   pygame.draw.rect(screen,pt,(200,200,800,400),0) 
   finfire(x,y)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         gameExit = True
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            gameExit = True


def Jelly(x,y):
   screen.blit(candy,(x,y))
x = 100
y = 550

def timegone():
   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_pressed()
   wb = xlrd.open_workbook("syno.xlsx")
   sh1 = wb.sheet_by_index(0)
   low_x = 1
   low_y = 0
   hig_x = 20
   hig_y = 1
   score = 0
   fail = 0
   RA = 0
   TE = 0
   lead_y = 0         		# start at y= .....
   lead_y_change = 3		# x moveing ifx=0=stop 
   gameExit = False
   keyword = 0
   while not gameExit :
      screen.fill(pink)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               gameExit = True
 		 # lead_x += lead_x_change 	#if adding +x = moving 
      lead_y += lead_y_change
      if lead_y > 600 :
         screen.fill(edpink)
      if lead_y > 799 :
         screen.fill(CRIMSON)
    	 lead_y_change = 0
         pygame.draw.rect(screen,CRIMSON,(155,170,600,450),0) 
         SCore(score,80,420,100)
         if event.type == MOUSEBUTTONDOWN:
            game_intro()
         
      else :
         pygame.draw.rect(screen,bbb,(0,lead_y,1200,800),0) # (x,y,w,h,thick)
         pygame.draw.rect(screen,pvr,(415,170,370,150),0) #input meaning
      if (TE == 0 and score == 0) or (RA == 1) :
         fianl_X = random.randint(low_x,hig_x)      #สุ่ม เลข 1-20
         fianl_XX = random.randint(low_x,hig_x)     # สุ่ม 1-20
         fianl_XXX = random.randint(low_x,hig_x)    # สุ่ม 1 - 20 
                                    #if (fianl_X ==  fianl_XX) or (fianl_X == fianl_XXX)
         for i in range(10):
            seeex = (sh1.cell(fianl_X,low_y).value)    #เลือกคอลัมที่0คือด้านซ้ายสุดสุ่มrow 1-20 จาก fianl_X
	    vocabex1 = (sh1.cell(fianl_XX,hig_y).value) 
            vocabex2 = (sh1.cell(fianl_XXX ,hig_y).value)
            if (fianl_X ==  fianl_XX) or (fianl_X == fianl_XXX):
               RA = 0 
               TE = 1
            else :
               keyword == 3
#""""
      if keyword == 3 and (fianl_X !=  fianl_XX) or (fianl_X != fianl_XXX):  
         seeex = (sh1.cell(fianl_X,low_y).value)    #เลือกคอลัมที่0คือด้านซ้ายสุดสุ่มrow 1-20 จาก fianl_X
	 vocabex1 = (sh1.cell(fianl_XX,hig_y).value) 
         vocabex2 = (sh1.cell(fianl_XXX ,hig_y).value)
      elif (fianl_X ==  fianl_XX) or (fianl_X == fianl_XXX):          
         RA = 0 
         TE = 1  
#""""  ส่วนนี้ใส่ไม่ใส่ก็ได้ 

      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      if 450+300 > mouse[0] > 450 and 390+100 > mouse[1] > 390 :
         pygame.draw.rect(screen,wh,(450,390,300,100),0) #input vocab
         if event.type == MOUSEBUTTONDOWN:
            keyword = 1
            if fianl_X ==  fianl_XX :
               keyword = 1
            else :
               keyword = 2
            
      else:
         pygame.draw.rect(screen,dt,(450,390,300,100),0) #input vocab
      smallText = pygame.font.Font("freesansbold.ttf",28)
      textSurf, textRect = randomna(vocabex1, smallText)
      textRect.center = ( (450+(300/2)), (390+(100/2)) )
      screen.blit(textSurf, textRect)

      if 450+300 > mouse[0] > 450 and 520+100 > mouse[1] > 520 :
         pygame.draw.rect(screen,wh,(450,520,300,100),0) #input vocab 
         if event.type == MOUSEBUTTONDOWN:
            keyword = 1
            if fianl_X ==  fianl_XXX :
               keyword = 1
            else :
               keyword = 2
         
     
      else:
         pygame.draw.rect(screen,dt,(450,520,300,100),0) #input vocab
      smallText = pygame.font.Font("freesansbold.ttf",28)
      textSurf, textRect = randomna(vocabex2, smallText)
      textRect.center = ( (450+(300/2)), (520+(100/2)) )
      screen.blit(textSurf, textRect)

      smallText = pygame.font.Font("freesansbold.ttf",50)   ###  ของรันดอม
      textSurf, textRect = dd(seeex, smallText)
      textRect.center = ( 600, 250 )
      screen.blit(textSurf, textRect)


      if (keyword == 1 or keyword == 2 or keyword == 3) and event.type == MOUSEBUTTONUP :
         lead_y = 0        	 #lead_y = 0 return to pointy=50now if keyup
         if keyword == 1 :
            score += 1
         if keyword == 2:
            fail += 1
         RA = 1 
         if score == 5 :
            lead_y_change += 2.5
         if score == 10 : 
            lead_y_change += 2
	 if score == 30 :
            lead_y_change += 2
	 if score == 40 :
	    lead_y_change += 2
     	 keyword = 0



      Jelly(x,y)
      buttonback(playgame) 
      Fail(fail)
      SCore(score,40,10,5)

      pygame.display.update()
      clock.tick(30)


#def superrandom()

   
def playgame():
   gameExit = False
   while not gameExit :
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True    

      screen.fill(Mistryrose)

      buttonback(game_intro)
      buttonplaygame("VOCABULARY",460,140,280,80,wh,stbluer,playvocabulary)
      buttonplaygame("SYNONYMS",460,300,280,80,wh,stbluer,timegone)
      buttonplaygame("ANTONYMS",460,440,280,80,wh,stbluer,timegone)
      buttonplaygame("TOP TOEIC",460,580,280,80,wh,stbluer,timegone)


      pygame.display.update()
      clock.tick(15)

def playvocabulary():
   gameExit = False
   while not gameExit :
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True    

      screen.fill(greensoft)
      screen.blit(princess,(30,420))

      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      buttonback(see)

      buttonplaygame("A  B",450,60,280,80,salmon,stbluer,vocabulary)
      buttonplaygame("C  D",450,200,280,80,salmon,stbluer,see)
      buttonplaygame("E  F",450,340,280,80,salmon,stbluer,game_intro)
      buttonplaygame("G  H",450,480,280,80,salmon,stbluer,game_intro)
      buttonplaygame("I J K",450,600,280,80,salmon,stbluer,timegone)

      pygame.display.update()
      clock.tick(10)


def SCore(count,u,x,y):
   font = pygame.font.SysFont(None,u)
   text = font.render("  SCORE : " +str(count),True,bla)
   screen.blit(text,(x,y))


#def ransyno():
 #     if RA == 0 :
  #       for i in range(1):
   #         RANsyno = (random.choice(thesyno))
    #        smallText = pygame.font.Font("freesansbold.ttf",50)
     #       textSurf, textRect = dd(RANsyno, smallText)
      #    textRect.center = ( 200, 200 )
        #    screen.blit(textSurf, textRect)
       #     RA = 1 
   
def Fail(count):
   font = pygame.font.SysFont(None,40)
   text = font.render("  FAIL     : " +str(count),True,bla)
   screen.blit(text,(5,30))

def qq():
   pygame.quit() 
   quit()


def see() :
   gameExit = False
   while not gameExit :
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True    

      screen.fill(papayawhip)
      vocab("V O C A B U L A R Y")
      screen.blit(snail,(30,420))

      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      buttonback(game_intro)

      buttonsee("VOCABULARY",300,200,280,80,wh,stbluer,vocabulary)
      buttonsee("SYNONYMS",300,340,280,80,wh,stbluer,synonyms)
      buttonsee("ANTONYMS",300,480,280,80,wh,stbluer,anto)
      buttonsee("FIND VOCAB",750,200,280,80,pvr,stbluer,findvocab)
   
      buttonintro ("QUIT",860,560,240,80,dt,stbluer,qq)
      buttonintro ("PLAY",860,450,240,80,dt,stbluer,playgame)

      pygame.display.update()
      clock.tick(10)



def vocabulary():

   gameExit = False
   while not gameExit :
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True    

      screen.fill(bff)
      screen.blit(snail,(30,420))

      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      buttonback(see)

      buttonplaygame("1. A  B",300,60,280,80,wh,stbluer,A)
      buttonplaygame("2. C  D",300,200,280,80,wh,stbluer,see)
      buttonplaygame("3. E  F",300,340,280,80,wh,stbluer,game_intro)
      buttonplaygame("4. G  H",300,480,280,80,wh,stbluer,game_intro)
      buttonplaygame("5. I J K",300,600,280,80,wh,stbluer,timegone)

      pygame.display.update()
      clock.tick(10)

def A ():

   gameExit = False
   while not gameExit :
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True    

      screen.fill(bff)
      
      vocaaa("ability",120,75)  
   #   vo("ความสามารถ",300,75)
      vocaaa("abroad",120,145)  
    #  vo("ในต่างประเทศ",300,115)
      vocaaa("absolutely",120,215)  
   #   vo("อย่างแน่นอน",300,130)
      vocaaa("accept",120,285)  
    #  vo("ยอมรับ",300,145)
      vocaaa("access",120,355)  
     # vo("วิธีเข้าถึง",300,160)
      vocaaa("accessible",120,425)  
     # vo("เข้าไปได่ง้าย",300,160)
      vocaaa("accident",120,495)  
     # vo("เหตุบังเอิญ",300,160)
      vocaaa("accommodate",120,565)  
     # vo("จัดให้เหมาะ",300,160)
      vocaaa("according",120,635)  
     # vo("ที่ยอมรับร่วมกัน",300,160)
      vocaaa("accounting",120,705)  
     # vo("หลักการบัญชี",300,160)
      vocaaa("baggage",650,75)  
     # vo("กระเป๋าเดินทาง",300,160)
      vocaaa("balance",650,145)  
     # vo("ความสมดล",300,160)
      vocaaa("bank",650,215)  
     # vo("ธนาคาร",300,160)
      vocaaa("bankrupt",650,285)  
     # vo("ล้มละลาย",300,160)
      vocaaa("bargain",650,355)  
     # vo("การต่อรอง",300,160)
      vocaaa("basic",650,425)  
     # vo("พื้นฐาน",300,160)
      vocaaa("belongings",650,495)  
     # vo("ทรัพยสิน",300,160)
      vocaaa("beneficial",650,565)  
     # vo("เป็นประโยชน์",300,160)
      vocaaa("benefit",650,635)  
     # vo("ผลประโยชนน์",300,160)
      vocaaa("beverage",650,705)  
     # vo("เครื่องดื่ม",300,160)





      buttonback(see)

      pygame.display.update()
      clock.tick(10)

   pygame.quit() 
   quit()



def synonyms():

   gameExit = False
   while not gameExit :
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True    

      screen.fill(bff)
      screen.blit(jelly,(450,400))

      vocaaa("AMAZING",120,75)  
      voa("INCREDIBLE",300,75)
      vocaaa("ANGEY",120,145)  
      voa("FURIOUS",300,145)
      vocaaa("ANSWER",120,215)  
      voa("RESPOND",300,215)
      vocaaa("ASK",120,285)  
      voa("REQUEST",300,285)
      vocaaa("AWFUL",120,355)  
      voa("TERRIBLE",300,355)
      vocaaa("BAD",120,425)  
      voa("WICKED",300,425)
      vocaaa("BEAUTIFU",120,495)  
      voa("ATTRACTIVE",300,495)
      vocaaa("BEGIN",120,565)  
      voa("START",300,565)
      vocaaa("BIG",120,635)  
      voa("EGNORMOUS",300,635)
      vocaaa("BRAVE",120,705)  
      voa("COURAGEOUS",300,705)
      vocaaa("COOL",650,75)  
      voa("FROSTY",830,75)
      vocaaa("DENGEROUS",650,145)  
      voa("UNSAFE",830,145)
      vocaaa("DARK",650,215)  
      voa("SHADOWY",830,215)
      vocaaa("END",650,285)  
      voa("CONCLUDE",830,285)
      vocaaa("ENJOY",650,355)  
      voa("BE PLEASED",830,355)
      vocaaa("FALL",650,425)  
      voa("DROP",830,425)
      vocaaa("FAMOUS",650,495)  
      voa("WELL-KNOWN",830,495)
      vocaaa("FAST",650,565)  
      voa("QUICK",830,565)
      vocaaa("GOOD",650,635)  
      voa("EXCELLENT",830,635)
      vocaaa("HATE",650,705)  
      voa("DISLIKE",830,705)


      buttonback(see)



      pygame.display.update()
      clock.tick(10)

   pygame.quit() 
   quit()

def anto():

   gameExit = False
   while not gameExit :
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True    

      screen.fill(salmon)
      screen.blit(cubcake,(20,40))


      buttonback(see)

      pygame.display.update()
      clock.tick(10)

   pygame.quit() 
   quit()



def findvocab():
   gameExit = False
   while not gameExit :
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True    
      search()
      screen.fill(bff)
      screen.blit(princess,(30,20))


      buttonback(game_intro)
      pygame.display.update()
      clock.tick(10)

   pygame.quit() 
   quit()


def s():
   qq()   



def buttonback(n):
      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      if 1000+100 > mouse[0] > 1000 and 680+70 > mouse[1] > 680 :
         pygame.draw.rect(screen,liam,(1000,680,100,70),0) #input back
         if click[0] == 1 and n != None:
            n()
      else:
         pygame.draw.rect(screen,dt,(1000,680,100,70),0) #input back
      smallText = pygame.font.Font("freesansbold.ttf",28)
      textSurf, textRect = back("BACK", smallText)
      textRect.center = ( (1000+(100/2)), (680+(70/2)) )
      screen.blit(textSurf, textRect)   



def buttonintro(text,x,y,w,h,ic,ac,nq):
      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      if x+w > mouse[0] > x and y+h > mouse[1] > y :  
         pygame.draw.rect(screen,ac,(x,y,w,h)) #quit
         if click[0] == 1 and nq != None:
            nq()
      else:
         pygame.draw.rect(screen,ic,(x,y,w,h)) #quit
      smallText = pygame.font.Font("freesansbold.ttf",35)
      textSurf, textRect = dd(text, smallText)
      textRect.center = ( (x+(w/2)), (y+(h/2)) )
      screen.blit(textSurf, textRect)



def buttonplaygame(text,x,y,w,h,ic,ac,nrt): #n=name of def
      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      if x+w > mouse[0] > x and y+h > mouse[1] > y :
         pygame.draw.rect(screen,ac,(x,y,w,h)) #quit
         if click[0] == 1 and nrt != None:
            nrt()  
      else:
         pygame.draw.rect(screen,ic,(x,y,w,h)) #quit
      smallText = pygame.font.Font("freesansbold.ttf",35)
      textSurf, textRect = dd(text, smallText)
      textRect.center = ( (x+(w/2)), (y+(h/2)) )
      screen.blit(textSurf, textRect)


def buttonsee(text,x,y,w,h,ic,ac,ne): #n=name of def
      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      if x+w > mouse[0] > x and y+h > mouse[1] > y :
         pygame.draw.rect(screen,ac,(x,y,w,h)) #quit
         if click[0] == 1 and ne != None:
            ne()  
      else:
         pygame.draw.rect(screen,ic,(x,y,w,h)) #quit
      smallText = pygame.font.Font("freesansbold.ttf",35)
      textSurf, textRect = dd(text, smallText)
      textRect.center = ( (x+(w/2)), (y+(h/2)) )
      screen.blit(textSurf, textRect)



def message_to_screen(text):
   largeText = pygame.font.Font('freesansbold.ttf',90)
   textSurf, textRect = text_objects(text,largeText)
   textRect.center = (600,150)
   screen.blit(textSurf,textRect)

def text_objects(text,font):
   textSurface = font.render(text,True,dodgerblue)
   return textSurface , textSurface.get_rect()

def ee(text,font): #in defsee
   textSurface = font.render(text,True,white)
   return textSurface , textSurface.get_rect()


def ff(text,font): #in top toeiv
   textSurface = font.render(text,True,white)
   return textSurface , textSurface.get_rect()


def antotext(text,font): #in defsee
   textSurface = font.render(text,True,white)
   return textSurface , textSurface.get_rect()

def dd(text,font):
   textSurface = font.render(text,True,white)
   return textSurface , textSurface.get_rect()

def vocab(text):
   largeText = pygame.font.Font('freesansbold.ttf',75)
   textSurf, textRect = d(text,largeText)
   textRect.center = (600,120)
   screen.blit(textSurf,textRect)

def d(text,font):
   textSurface = font.render(text,True,wh)
   return textSurface , textSurface.get_rect()


def back(text,font):
   textSurface = font.render(text,True,white)
   return textSurface , textSurface.get_rect()


def mes(text):
   largeText = pygame.font.Font('freesansbold.ttf',40)
   textSurf, textRect = textob(text,largeText)
   textRect.center = (600,260)
   screen.blit(textSurf,textRect)

def textob(text,font):
   textSurface = font.render(text,True,pvr )
   return textSurface , textSurface.get_rect()


def vocaaa(text,x,y):
   largeText = pygame.font.Font('freesansbold.ttf',30)
   textSurf, textRect = vooo(text,largeText)
   textRect.center = (x,y)
   screen.blit(textSurf,textRect)

def vooo(text,font):
   textSurface = font.render(text,True,pvr )
   return textSurface , textSurface.get_rect()


def voa(text,x,y):
   largeText = pygame.font.Font('freesansbold.ttf',30)
   textSurf, textRect = ui(text,largeText)
   textRect.center = (x,y)
   screen.blit(textSurf,textRect)
def ui(text,font):
   textSurface = font.render(text,True,dodgerblue )
   return textSurface , textSurface.get_rect()


def vo(text,x,y):
   largeText = pygame.font.Font('tahoma.ttf',30)
   textSurf, textRect = vooo(text,largeText)
   textRect.center = (x,y)
   screen.blit(textSurf,textRect)

def randomna(text,font):             #.ใส่ข้อความสุ่ม
   textSurface = font.render(text,True,white)
   return textSurface , textSurface.get_rect()


  # for i in range(1):
  #    RANsyno = (random.choice(thesyno))
   #   smallText = pygame.font.Font("freesansbold.ttf",35)
  #    textSurf, textRect = dd(RANsyno, smallText)
  #    textRect.center = ( (x+(w/2)), (y+(h/2)) )
  #    screen.blit(textSurf, textRect)
   #   break;

















game_intro()

