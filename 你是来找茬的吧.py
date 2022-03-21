import pygame
import time

def is_in_rect(x,y,x_position,y_position,width,hight):
    if x_position<=x<=x_position+width and y_position<=y<=y_position+hight:
        return True
    return False            #判断是否在矩形区域内
def knife_play(s):
    image = [pygame.image.load('knife/knife_%d.png'%i) for i in range(1,18)]
    for fig in image:
        screen.blit(knife_background, (0, 0))
        if s == 1:
            screen.blit(font_error.render('× %d' % (error_1+1), True, (139, 69, 19)), (850, 570))
        else:
            screen.blit(font_error.render('× %d' % (error_2 + 1), True, (139, 69, 19)), (850, 570))
        screen.blit(fig,(0,-35))
        pygame.display.flip()
        time.sleep(0.012)
    return None             #播放扔刀动画

pygame.init()
pygame.display.set_caption("你是来找茬的吧？")        #设置窗口标题
screen = pygame.display.set_mode((1080,640))    #设置窗口大小

cover = pygame.image.load('cover.png')          #加载封面图片
cover_start = pygame.image.load('cover_start.png')          #加载开始按钮图片
stage1 = pygame.image.load('stage1.png').convert()
stage2 = pygame.image.load('stage2.png').convert()      #加载背景图片
fig1A = pygame.image.load('fig1A.png').convert()    #加载场景1左侧图片
fig1B = pygame.image.load('fig1B.png').convert()    #加载场景1右侧图片
fig2A = pygame.image.load('fig2A.png').convert()    #加载场景2左侧图片
fig2B = pygame.image.load('fig2B.png').convert()    #加载场景2右侧图片

time_limit = 50
timer_event = pygame.USEREVENT+1
timer1 = pygame.image.load('timer1.png')       #加载计时器背景
timer2 = pygame.image.load('timer2.png')
gua = pygame.image.load('gua.png')       #加载计时器小图标
font_timer = pygame.font.SysFont('Arial', 30,True)      #加载计时器字体
pygame.time.set_timer(timer_event, 1000)        #计时器

error_1 = 5
error_2 = 5
is_error_1 = [False,False,False,False,False]
is_error_2 = [False,False,False,False,False]
circle = pygame.image.load('circle.png')
font_error = pygame.font.SysFont('华光胖头鱼_CNKI', 80,True)
error = pygame.image.load('error.png')
knife_background = pygame.image.load('knife_background.png')

mode = 2
win_gua = pygame.image.load('win_gua.png')
win_qiang = pygame.image.load('win_qiang.png')
next_text = pygame.image.load('next_text.png')
box = pygame.image.load('box.png')
baipiao = pygame.image.load('biapiao.png')
baipiao_position = 0     #记录可移动选项“白嫖”的上下位置
choose = pygame.image.load('choose.png')
fail = pygame.image.load('fail.png')
win_final = pygame.image.load('win_final.png')

sound_play = True
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1,0)
cover_sound = pygame.mixer.Sound('你要找茬是不是啊.mp3')
start_sound = pygame.mixer.Sound('我肯定要啊.mp3')
error_1_1_sound = pygame.mixer.Sound('生瓜蛋子.mp3')
error_1_2_sound = pygame.mixer.Sound('你贤惠.mp3')
error_1_3_sound = pygame.mixer.Sound('异形.mp3')
error_1_4_sound = pygame.mixer.Sound('象鸣.mp3')
error_1_5_sound = pygame.mixer.Sound('振涛.mp3')
win_sound = pygame.mixer.Sound('win_sound.mp3')
next_sound = pygame.mixer.Sound('行.mp3')
toubi_sound = pygame.mixer.Sound('满意了吧.mp3')
fail_sound = pygame.mixer.Sound('fail.mp3')
error_2_1_sound = pygame.mixer.Sound('瓜粒子.mp3')
error_2_2_sound = pygame.mixer.Sound('劈瓜.mp3')
error_2_3_sound = pygame.mixer.Sound('水果摊.mp3')
error_2_4_sound = pygame.mixer.Sound('吸铁石.mp3')
error_2_5_sound = pygame.mixer.Sound('whatsup.mp3')

done = False
close = False
screen.blit(cover, (0, 0))
pygame.display.flip()
while (not done) and (not close):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True             #控制窗口关闭
        elif event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()  # 获取鼠标位置
            if is_in_rect(mouse_position[0], mouse_position[1], 460, 220, 410, 390):
                if is_in_rect(mouse_position[0], mouse_position[1], 605, 475, 150, 150):
                    screen.blit(cover_start, (0, 0))
                    is_cover_start = True           #鼠标移动至小瓜时显示大瓜开始按钮
                    if sound_play:
                        cover_sound.play()
                        sound_play = False
            else:
                screen.blit(cover, (0, 0))
                is_cover_start = False              #鼠标离开时开始按钮消失
                sound_play = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_cover_start and is_in_rect(event.pos[0],event.pos[1],460,220,410,390):
                screen.blit(cover, (0, 0))
                screen.blit(cover_start, (0, 20))
                pygame.display.flip()
                start_sound.play()
                time.sleep(0.2)
                done = True                         #点击开始按钮后，按钮下移，同时切换场景
    pygame.display.flip()

done = False
screen.blit(stage1, (0, 0))
screen.blit(fig1A, (50, 100))
screen.blit(fig1B, (580, 100))           #展示第一关图片
while (not done) and (not close):
    screen.blit(error, (0, 0))
    screen.blit(font_error.render('× %d' % (error_1), True, (139, 69, 19)), (850, 570))
    if error_1 == 0:
        mode = 1
        done = True
        pygame.image.save(screen,'tem.png')
        win_background = pygame.image.load('tem.png')
    elif time_limit == 0:
        mode = 0
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True         #控制窗口关闭
        elif event.type == timer_event :
            if error_1 != 0:
                time_limit -= 1
            if time_limit == 0:
                pygame.time.set_timer(timer_event, 0)       #倒计时器
            screen.blit(timer1, (0, 0))
            if time_limit >= 25:
                pygame.draw.rect(screen, (111, 151, 200), (801, 35, 4 * time_limit, 10))
                pygame.draw.rect(screen, (62, 129, 223), (801, 45, 4 * time_limit, 10))
                screen.blit(font_timer.render(str(time_limit), True, (90, 130, 210)), (754, 25))
            if 10 <= time_limit < 25:
                pygame.draw.rect(screen, (180, 155, 56), (801, 35, 4 * time_limit, 10))
                pygame.draw.rect(screen, (180, 132, 40), (801, 45, 4 * time_limit, 10))
                screen.blit(font_timer.render(str(time_limit), True, (180, 140, 50)), (754, 25))
            if time_limit < 10:
                pygame.draw.rect(screen, (209, 107, 143), (801, 35, 4 * time_limit, 10))
                pygame.draw.rect(screen, (180, 40, 43), (801, 45, 4 * time_limit, 10))      #计时条随时间减少变短并变色
                screen.blit(font_timer.render(str(time_limit), True, (239, 65, 54)), (762, 25))
            screen.blit(gua, (791+4*time_limit, 35))        #小西瓜随计时条移动
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (is_in_rect(event.pos[0], event.pos[1], 53, 301, 47, 26) or is_in_rect(event.pos[0], event.pos[1],53 + 530, 301, 47, 26)) & (not is_error_1[0]):
                error_1 -= 1
                is_error_1[0] = True
                screen.blit(circle, (44, 283))
                screen.blit(circle, (44 + 530, 283))
                error_1_1_sound.play()
                knife_play(1)
            if (is_in_rect(event.pos[0], event.pos[1], 194, 458, 115, 45) or is_in_rect(event.pos[0], event.pos[1],194 + 530, 458, 115, 45)) & (not is_error_1[1]):
                error_1 -= 1
                is_error_1[1] = True
                screen.blit(circle, (238, 452))
                screen.blit(circle, (238 + 530, 452))
                error_1_2_sound.play()
                knife_play(1)
            if (is_in_rect(event.pos[0], event.pos[1], 348, 284, 47, 53) or is_in_rect(event.pos[0], event.pos[1],348 + 530, 284, 47, 53)) & (not is_error_1[2]):
                error_1 -= 1
                is_error_1[2] = True
                screen.blit(circle, (338, 283))
                screen.blit(circle, (338 + 530, 283))
                error_1_3_sound.play()
                knife_play(1)
            if (is_in_rect(event.pos[0], event.pos[1], 406, 419, 25, 23) or is_in_rect(event.pos[0], event.pos[1],406 + 530, 419, 25, 23)) & (not is_error_1[3]):
                error_1 -= 1
                is_error_1[3] = True
                screen.blit(circle, (389, 403))
                screen.blit(circle, (389 + 530, 403))
                error_1_4_sound.play()
                knife_play(1)
            if (is_in_rect(event.pos[0], event.pos[1], 409, 182, 53, 72) or is_in_rect(event.pos[0], event.pos[1],409 + 530, 182, 53, 72)) & (not is_error_1[4]):
                error_1 -= 1
                is_error_1[4] = True
                screen.blit(circle, (398, 199))
                screen.blit(circle, (398 + 530, 199))
                error_1_5_sound.play()
                knife_play(1)

done = False
if mode == 1:
    screen.blit(win_qiang, (0, 0))
    screen.blit(win_gua,(0,0))
    screen.blit(next_text, (-30, 0))
    win_sound.play()
    while (not done) and (not close):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_in_rect(event.pos[0], event.pos[1], 418, 377,293, 149):
                    screen.blit(win_background, (0, 0))
                    screen.blit(win_qiang, (0, 0))
                    screen.blit(win_gua,(0,20))
                    screen.blit(next_text, (-30, 20))
                    pygame.display.flip()
                    next_sound.play()
                    time.sleep(0.1)
                    screen.blit(win_background, (0, 0))
                    screen.blit(win_qiang, (0, 0))
                    screen.blit(win_gua, (0, 0))
                    screen.blit(next_text, (-30, 0))
                    screen.blit(box,(0,0))
                    screen.blit(baipiao, (0, 0))
                    done = True
    done = False
    while (not done) and (not close):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
            elif event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()  # 获取鼠标位置
                if is_in_rect(mouse_position[0], mouse_position[1], 708, 324, 110, 35) and baipiao_position == 0:
                    screen.blit(box, (0, 0))
                    screen.blit(baipiao, (0, -50))
                    baipiao_position = 1
                if is_in_rect(mouse_position[0], mouse_position[1], 708, 274, 110, 35) and baipiao_position == 1:
                    screen.blit(box, (0, 0))
                    screen.blit(baipiao, (0, 0))
                    baipiao_position = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_in_rect(event.pos[0], event.pos[1], 577, 325, 108, 34):
                    screen.blit(choose, (0, 0))
                    pygame.display.flip()
                    toubi_sound.play()
                    time.sleep(0.1)
                    done = True
if mode == 0:
    screen.blit(fail, (0,0))
    fail_sound.play()
    while (not done) and (not close):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True            #第一关结束

done = False
time_limit = 20
screen.blit(stage2, (0, 0))
screen.blit(fig2A, (50, 100))
screen.blit(fig2B, (580, 100))           #展示第二关图片
while (not done) and (not close):
    screen.blit(error, (0, 0))
    screen.blit(font_error.render('× %d' % (error_2), True, (139, 69, 19)), (850, 570))
    pygame.display.flip()
    if error_2 == 0:
        mode = 1
        done = True
        pygame.image.save(screen,'tem.png')
        win_background = pygame.image.load('tem.png')
    elif time_limit == 0:
        mode = 0
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True         #控制窗口关闭
        elif event.type == timer_event :
            if error_2 != 0:
                time_limit -= 1
            if time_limit == 0:
                pygame.time.set_timer(timer_event, 0)       #倒计时器
            screen.blit(timer2, (0, 0))
            if time_limit >= 10:
                pygame.draw.rect(screen, (111, 151, 200), (801, 35, 10 * time_limit, 10))
                pygame.draw.rect(screen, (62, 129, 223), (801, 45, 10 * time_limit, 10))
                screen.blit(font_timer.render(str(time_limit), True, (90, 130, 210)), (754, 25))
            if 5 <= time_limit < 10:
                pygame.draw.rect(screen, (180, 155, 56), (801, 35, 10 * time_limit, 10))
                pygame.draw.rect(screen, (180, 132, 40), (801, 45, 10 * time_limit, 10))
                screen.blit(font_timer.render(str(time_limit), True, (180, 140, 50)), (762, 25))
            if time_limit < 5:
                pygame.draw.rect(screen, (209, 107, 143), (801, 35, 10 * time_limit, 10))
                pygame.draw.rect(screen, (180, 40, 43), (801, 45, 10 * time_limit, 10))      #计时条随时间减少变短并变色
                screen.blit(font_timer.render(str(time_limit), True, (239, 65, 54)), (762, 25))
            screen.blit(gua, (791+10*time_limit, 35))        #小西瓜随计时条移动
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (is_in_rect(event.pos[0], event.pos[1], 67, 359, 41, 42) or is_in_rect(event.pos[0], event.pos[1],67+530,359,41,42)) & (not is_error_2[0]):
                error_2 -= 1
                is_error_2[0] = True
                screen.blit(circle, (56, 353))
                screen.blit(circle, (56 + 530, 353))
                error_2_1_sound.play()
                knife_play(2)
            if (is_in_rect(event.pos[0], event.pos[1], 193, 100, 52, 46) or is_in_rect(event.pos[0], event.pos[1],193 + 530, 100, 52, 46)) & (not is_error_2[1]):
                error_2 -= 1
                is_error_2[1] = True
                screen.blit(circle, (191, 91))
                screen.blit(circle, (191 + 530, 91))
                error_2_2_sound.play()
                knife_play(2)
            if (is_in_rect(event.pos[0], event.pos[1], 721-530, 491, 61, 36) or is_in_rect(event.pos[0], event.pos[1],721, 491, 61, 36)) & (not is_error_2[2]):
                error_2 -= 1
                is_error_2[2] = True
                screen.blit(circle, (721-530, 482))
                screen.blit(circle, (721, 482))
                error_2_3_sound.play()
                knife_play(2)
            if (is_in_rect(event.pos[0], event.pos[1],400,442,64,29) or is_in_rect(event.pos[0], event.pos[1],400+530,442,64,29)) & (not is_error_2[3]):
                error_2 -= 1
                is_error_2[3] = True
                screen.blit(circle, (392, 427))
                screen.blit(circle, (392 + 530, 427))
                error_2_4_sound.play()
                knife_play(2)
            if is_in_rect(event.pos[0], event.pos[1],507,11,59,67) & (not is_error_2[4]):
                error_2 -= 1
                is_error_2[4] = True
                screen.blit(circle, (503, 36))
                error_2_5_sound.play()
                knife_play(2)

done = False
if mode == 1:
    screen.blit(win_final, (0,0))
    win_sound.play()
    while (not done) and (not close):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
if mode == 0:
    screen.blit(fail, (0,0))
    fail_sound.play()
    while (not done) and (not close):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True