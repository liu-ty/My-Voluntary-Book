import pygame
import time
from functions import translate

class Selectbutton():
    def __init__(self,num,position,size):
        self.imgs = ['My Vocabulary Book/imgs/costume1.png',
                     'My Vocabulary Book/imgs/costume2.png',
                     'My Vocabulary Book/imgs/costume3.png',
                     'My Vocabulary Book/imgs/cb1.png',
                     'My Vocabulary Book/imgs/cb2.png',
                     'My Vocabulary Book/imgs/sb5.png',
                     'My Vocabulary Book/imgs/sb6.png',
                     'My Vocabulary Book/imgs/sb7.png',
                     'My Vocabulary Book/imgs/默写退出.png',
                     'My Vocabulary Book/imgs/sb9.png']
        self.id = num
        self.img = pygame.transform.scale(pygame.image.load(self.imgs[num]),size)
        self.position = position
        self.rect = self.img.get_rect()
        self.rect.left = self.position[0]
        self.rect.top = self.position[1]
    def draw_img(self,screen):
        screen.blit(self.img,self.rect)
    def touching(self,pos,status):
        if status == 0:
            if self.rect.collidepoint(pos):
                return True
            else:
                return False
        else:
                return False

class Timer():
    def __init__(self):
        self.fonts = pygame.font.Font('My Vocabulary Book/Verdana.ttf',20)
    def print_time(self,screen):
        self.times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.text = self.fonts.render(str(self.times),True,(255,255,255))
        screen.blit(self.text,(520,80))

class Addtexts():
    def __init__(self):
        self.fonts1 = pygame.font.Font('My Vocabulary Book/Verdana.ttf',20)
        self.fonts2 = pygame.font.Font('My Vocabulary Book/方正.ttf',20)
    def print_text(self,screen,eng,chi):
        self.engtext = self.fonts1.render(eng,True,(0,0,255))
        self.chitext = self.fonts2.render(chi,True,(0,0,255))
        screen.blit(self.engtext,(80,400))
        screen.blit(self.chitext,(80,450))

class Testprinter():
    def __init__(self):
        self.font = pygame.font.Font('My Vocabulary Book/方正.ttf',32)
    def handling(self,testlist,index):
        self.text = self.font.render(testlist[index],True,(0,0,0))
    def draw(self,screen):
        screen.blit(self.text,(60,200))
    def handling_ui(self,index,total,correct,start_tick,now_tick,finish):
        self.finisher = self.font.render('题目数:' + str(index) + '/' + str(total),True,(0,0,200))
        if not finish == 0:
            self.rater = self.font.render('正确率:' + str(round(correct/finish * 100,2))+'%',True,(0,0,200))
        else:
            self.rater = self.font.render('正确率:0.0%',True,(0,0,200))
        self.timers = self.font.render('用时:' + str(round((now_tick-start_tick)/16,1)) + 's',True,(0,0,200))
    def draw_ui(self,screen):
        screen.blit(self.finisher,(450,200))
        screen.blit(self.rater,(450,250))
        screen.blit(self.timers,(450,300))
class Judgeresult():
    def __init__(self):
        self.font = pygame.font.Font('My Vocabulary Book/方正.ttf',32)
        self.drawstatus = -1
    def draw(self,screen,inputtxt,answer,result,status):
        self.drawstatus -= 1
        if status == 0:
            self.render1 = self.font.render('你的答案是：'+inputtxt,True,(0,0,233))
            self.render2 = self.font.render('正确答案是：'+answer,True,(0,0,233))
            self.render3 = self.font.render('你的答案 '+result,True,(0,0,233))
            screen.blit(self.render1,(60,400))
            screen.blit(self.render2,(60,440))
            screen.blit(self.render3,(60,480))

class Test_score():
    def __init__(self):
        self.font1 = pygame.font.Font('My Vocabulary Book/方正.ttf',60)
        self.font2 = pygame.font.Font('My Vocabulary Book/方正.ttf',16)
    def calculate(self,rate,time,lenth):
        score = round(rate * 100,1)
        self.score = self.font1.render('得分:'+str(score),True,(240,0,0))
        self.process = self.font2.render('(按|左键|生成成绩单)',True,(0,0,0))
    def draw(self,screen):
        screen.blit(self.score,(50,200))
        screen.blit(self.process,(60,280))

class Showprinter():
    def __init__(self):
        self.font = pygame.font.Font('My Vocabulary Book/方正.ttf',40)
    def draw(self,screen,flist,slist):
        for i in range(8):
            new_frender = self.font.render(flist[i],True,(0,0,0))
            new_srender = self.font.render(slist[i],True,(0,0,233))
            screen.blit(new_frender,(50,100+i*50))
            screen.blit(new_srender,(450,100+i*50))
