# coding: utf8
import pygame
from pygame.locals import *
from random import randint
pygame.init()

# tela
a = 800
b = 600
a_dps = int(800)
b_dps = int(600-22)
screen = pygame.display.set_mode((a, b))

#variaveis gerais
running = 1
color = 255, 255, 255
x = y = 0
startPos=(0,0)
desenhar = 1

#variáveis de texto
texto = pygame.font.SysFont('comic sans ms', 15)


#variáveis do pincel
line_color = 0, 0, 0
line_size = 5

#tela de pintura
background = pygame.Surface((a_dps,b_dps))
background = background.convert()
background.fill((255,255,255))

#loop
while running:

    #imagens
    img_lapis = pygame.image.load("img/lapis.jpg")
    screen.blit(img_lapis, (0, 0))

    #seletores de cor
    pygame.draw.rect(screen, (255, 0, 0), [20, 0, 20, 20])
    pygame.draw.rect(screen, (255, 165, 0), [40, 0, 20, 20])
    pygame.draw.rect(screen, (255, 255, 0), [60, 0, 20, 20])
    pygame.draw.rect(screen, (177, 255, 47), [80, 0, 20, 20])
    pygame.draw.rect(screen, (0, 255, 0), [100, 0, 20, 20])
    pygame.draw.rect(screen, (46, 139, 87), [120, 0, 20, 20])
    pygame.draw.rect(screen, (0, 0, 255), [140, 0, 20, 20])
    pygame.draw.rect(screen, (0, 255, 255), [160, 0, 20, 20])

    #borracha_label
    borracha = texto.render("Borracha", True, (255, 255, 255))
    screen.blit(borracha, (730,0))

    #limpando tela_label
    clear = texto.render("Limpar Tela", True, (255, 255, 255))
    screen.blit(clear, (620,0))

    #troca de cores

    #preto
    if  x < 20 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 0, 0, 0
        line_size = 5

    #vermelho
    elif x > 20 and x < 40 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 255, 0, 0
        line_size = 5

    #laranja
    elif x > 40 and x < 60 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 255, 165, 0
        line_size = 5

    #amarelo
    elif x > 60 and x < 80 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 255, 255, 0
        line_size = 5

    #meio verde
    elif x > 80 and x < 100 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 177, 255, 47
        line_size = 5

    #verde
    elif x > 100 and x < 120 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 0, 255, 0
        line_size = 5

    #meio azul
    elif x > 120 and x < 140 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 46, 139, 87
        line_size = 5

    #azul
    elif x > 140 and x < 160 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 0, 0, 255
        line_size = 5

    #azul claro
    elif x > 160 and x < 180 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        line_color = 0, 255, 255
        line_size = 5

    #limpar a tela
    elif x > 620 and x <710 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        background.fill((255,255,255))

    #borracha
    if x > 730 and y < -2 and pygame.mouse.get_pressed()==(1,0,0):
        desenhar = 2
        line_color = 255, 255, 255

    #escolher opções
    pressionado = pygame.key.get_pressed()
    if pressionado[K_l]:
        desenhar = 1
    elif pressionado[K_p]:
        desenhar = 2

    #salvar imagem
    random = randint(0,300)
    if pressionado[K_s]:
        pygame.time.wait(2)
        salvar = pygame.image.save(background,'imagens_salvas/image_%d.png' % random)

    #desenhar

    #lapis
    if desenhar == 1:    
        for i in pygame.event.get():    
            if i.type == pygame.MOUSEMOTION:
                x,y = i.pos[0],(i.pos[1]-22)
                endPos = [x,y]
                if pygame.mouse.get_pressed()==(1,0,0):
                    pygame.draw.line(background, line_color, startPos, endPos, line_size)
                startPos=endPos    
        screen.blit(background,(0,22))

    #pincel
    elif desenhar == 2:
        for i in pygame.event.get():    
            if i.type == pygame.MOUSEMOTION:
                x,y = i.pos[0],(i.pos[1]-22)
                endPos = [x,y]
                if pygame.mouse.get_pressed()==(1,0,0):
                    pygame.draw.circle(background, line_color, (x,y), 20, 0)
                startPos=endPos    
        screen.blit(background,(0,22))
    
    #fechar a aplicação
    for i in pygame.event.get():
        if i.type == QUIT:
            running = 0

    #retorno ao início
    pygame.display.flip()
            
