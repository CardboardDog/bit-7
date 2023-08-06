import pygame
import colors
import random
import sys
import assetmanager
disp = pygame.display.set_mode((960,544))
running = True
mode = 1
sprites = [([0]*480)]*1
for i in range(272):
    sprites.append([0]*480)
x=0
y=0
sprites[2][5]=1
sprites[3][5]=4
sprites[4][5]=2
sprites[5][5]=3
sprites[1][5]=5
sprites[0][5]=6
s_color = 0
#for i in range(50):
#    sprites[2][5]=1
#print(sprites)
try:
    assetmanager.extract_assets()
except:
    pass
while(running):
    pygame.display.update()
    pygame.display.flip()
    disp.fill((0,0,0))
    pygame.draw.rect(disp,(25,25,25),(0,0,200,50))
    pygame.draw.rect(disp,(25,25,25),(200,0,200,50))
    pygame.draw.rect(disp,(25,25,25),(400,0,200,50))
    pygame.draw.rect(disp,(25,25,25),(600,0,200,50))
    rx=0
    ry=51
    dx=0
    dy=0
    m_pos = pygame.mouse.get_pos()
    m_pressed = pygame.mouse.get_pressed()[0]
    if mode == 1:
        for row in sprites:
            for colum in row:
                disp.set_at((rx,ry),pygame.Color(colors.color_codes[colum]))
                #print(rx)
                rx+=1
            ry+=1
            rx=0
        pygame.draw.rect(disp,(255,255,255),(0,51,16,16),1,0)
        for y in range(16):
            for x in range(16):
                if(m_pressed and ((481+x*17)<m_pos[0]) and ((481+x*17)+17>m_pos[0])):
                    if(((51+y*17)<m_pos[1]) and ((51+y*17)+17>m_pos[1])):
                        sprites[dy+y][dx+x]=s_color
                pygame.draw.rect(disp,pygame.Color(colors.color_codes[sprites[dy+y][dx+x]]),(481+x*17,51+y*17,17,17))
        for i in range(8):
            if(m_pressed):
                if((m_pos[0]>(481+(34*i))) and (m_pos[0]<(481+(34*i)+34))):
                   if((m_pos[1]>(51+16*17)) and (m_pos[1]<((51+16*17)+34))):
                        s_color = i
            pygame.draw.rect(disp,pygame.Color(colors.color_codes[i]),(481+(34*i),51+16*17,34,34))
            if(i==s_color):
                pygame.draw.rect(disp,(255,255,255),(481+(34*i),51+16*17,34,34),1,0)
        for i in range(8):
            pygame.draw.rect(disp,pygame.Color(colors.color_codes[i+8]),(481+(34*i),323+34,34,34))
            if(m_pressed):
                if((m_pos[0]>(481+(34*i))) and (m_pos[0]<(481+(34*i)+34))):
                   if((m_pos[1]>(323+34)) and (m_pos[1]<((323+34)+34))):
                        s_color = i+8
            if(i+8==s_color):
                pygame.draw.rect(disp,(255,255,255),(481+(34*i),323+34,34,34),1,0)
                
    for i in pygame.event.get():
        if(i.type == pygame.QUIT):
            running = False
pygame.quit()
assetmanager.close_assets()
sys.exit()