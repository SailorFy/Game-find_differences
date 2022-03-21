import pygame
import time

def knife_play():
    image = [pygame.image.load('knife/knife_%d.png'%i) for i in range(1,18)]
    for fig in image:
        screen.blit(stage1, (0, 0))
        screen.blit(fig,(0,-35))
        pygame.display.flip()
        time.sleep(0.015)
    return None

pygame.init()
pygame.display.set_caption("你是来找茬的吧？")        #设置窗口标题
screen = pygame.display.set_mode((1080,640))
stage1 = pygame.image.load('stage1.png').convert()    #加载背景图片
fig1A = pygame.image.load('fig1A.png').convert()    #加载场景1左侧图片
fig1B = pygame.image.load('fig1B.png').convert()    #加载场景1右侧图片

time_limit = 100
timer_event = pygame.USEREVENT+1
timer1 = pygame.image.load('timer1.png')
font_timer = pygame.font.SysFont('Arial', 30,True)
pygame.time.set_timer(timer_event, 1000)        #计时器


error_1 = 5
is_error_1 = [False,False,False,False,False]
circle = pygame.image.load('circle.png')
font_error = pygame.font.SysFont('华光胖头鱼_CNKI', 80,True)
error1 = pygame.image.load('error_1.png')

win_background = pygame.image.load('win_background.png').convert_alpha()

done = False
screen.blit(stage1, (0, 0))
screen.blit(fig1A, (50, 100))
screen.blit(fig1B, (580, 100))           #展示第一关图片
pygame.display.flip()

while (not done):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True         #控制窗口关闭
        pygame.display.flip()