import pygame
import sys
import random
import time


screen_width=1090
screen_height=600
# game initialisation
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = True

# color for plaryers
cyan = (0, 204, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (174, 0, 99)
white = (255, 255, 255)
black = (0, 0, 0)


# drawing board
def board():
    origin = 200
    pos_x = origin
    pos_y = origin
    for i in range(0, 5):
        for i in range(0, 5):
            pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, 50, 50), 5)
            pos_x += 50
        pos_y += 50
        pos_x = origin
    pos_x = origin
    pos_y = origin
    for i in range(0, 3):
        if i == 0:
            pos_x += 100
            pygame.draw.rect(screen, (0, 0, 255), (pos_x, pos_y, 50, 50), 5)
        elif i == 1:
            pos_y += 100
            pos_x = origin
            for i in range(0, 3):
                pygame.draw.rect(screen, (0, 0, 255), (pos_x, pos_y, 50, 50), 5)
                pos_x += 100
        elif i == 2:
            pos_x = origin + 100
            pos_y = origin + 200
            pygame.draw.rect(screen, (0, 0, 255), (pos_x, pos_y, 50, 50), 5)


# print text on buttons
def text_object(text, font,color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


# player class
class player(object):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.__buffer=[]
        self.__bufstatua=None

    def draw(self, x):
        pygame.draw.rect(screen, self.color, (x[0], x[1], self.width, self.height), 5)

    def set_pos(self,value):
        self.__buffer=list(value)
    def get_pos(self):
        return self.__buffer
    def set_butn_status(self,value):
        self.__bufstatua=value
    def get_butn_status(self):
        return self.__bufstatua


# initilising the players
player1 = player(10, 10, cyan)
player2 = player(10, 10, yellow)


#about page
def about():
    about = True
    # displaying name of the game
    font2 = pygame.font.Font('freesansbold.ttf', 50)
    about_surf, about_rect = text_object('working on it!!!', font2, (0, 0, 0))
    about_rect.center = ((screen_width / 2), (screen_height / 4))

    while about:

        screen.fill((217, 223, 185))

        screen.blit(about_surf,about_rect)


        pygame.display.update()


#game introduction
def gameintro():
    intro=True
    #displaying name of the game
    font2=pygame.font.Font('freesansbold.ttf',50)
    text_surf,text_rect=text_object('CHOUKA-BHARA',font2,(0,0,0))
    text_rect.center=((screen_width/2),(screen_height/4))

    #menu text
    font3 = pygame.font.Font('freesansbold.ttf', 30)
    start_surf,start_rect=text_object('START',font3,(255,255,255))
    start_rect.center=((545),(270))
    know_surf, know_rect = text_object('ABOUT', font3, (255, 255, 255))
    know_rect.center = ((545), (390))
    exit_surf, exit_rect = text_object('EXIT', font3, (255, 255, 255))
    exit_rect.center = ((545), (510))

    #list values of menu field
    lst=[240,360,480]




    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if click[0]==1 and 445+200>mouse[0]>445 and 240+60>mouse[1]>240:
            gameEngine()
        elif click[0]==1 and 445+200>mouse[0]>445 and 360+60>mouse[1]>360:
            about()
        elif click[0] == 1 and 445 + 200 > mouse[0] > 445 and 480 + 60 > mouse[1] > 480:
            sys.exit()







        screen.fill((217, 223, 185))

        screen.blit(text_surf,text_rect)


        #drawing menu

        pygame.draw.rect(screen,(0,0,0),(445,240,200,60))
        pygame.draw.rect(screen, (0, 0, 0), (445,360, 200, 60))
        pygame.draw.rect(screen, (0, 0, 0), (445,480, 200, 60))
        for i in lst:
            if 445<=mouse[0]<=445+200 and i<=mouse[1]<=i+60:
                pygame.draw.rect(screen, (105,105,105), (445, i, 200, 60))





        # text on menu
        screen.blit(start_surf, start_rect)
        screen.blit(know_surf, know_rect)
        screen.blit(exit_surf, exit_rect)



        pygame.display.update()
        clock.tick(30)




# function of game engine
def gameEngine():
    # cordinates for the players
    player1_pos = [[310, 460], [330, 460], [310, 480], [330, 480]]
    player2_pos = [[310, 160], [330, 160], [310, 180], [330, 180]]

    # player home cordinates
    home_1_pos = [[310, 460], [330, 460], [310, 480], [330, 480]]
    home_2_pos = [[310, 160], [330, 160], [310, 180], [330, 180]]

    # player home dict
    home_1 = {0: True, 1: True, 2: True, 3: True}
    home_2 = {0: True, 1: True, 2: True, 3: True}

    # players status to move
    status = None
    dicestatus = None

    # dice choices
    dice = [1, 2, 3, 4, 8]

    to=0

    # enabling the player"s flag to print
    enable1 = [True, True, True, True]
    enable2 = [True, True, True, True]

    # value of pawns at home
    home_counter_1 = 4
    home_counter_2 = 4

    # collision flag
    counter_player_1 = 0
    counter_player_2 = 0

    # if home pawn is clicked after eight or four
    def ishomepawn(pos):
        flag = None
        player1 = [[310, 460], [330, 460], [310, 480], [330, 480]]
        player2 = [[310, 160], [330, 160], [310, 180], [330, 180]]
        if status:
            for i in player1:
                if i == pos:
                    flag = True
                    break
                else:
                    flag = False
            return flag, player1.index(i)

        else:
            for i in player2:
                if i == pos:
                    flag = True
                    break
                else:
                    flag = False
            return flag, player2.index(i)

    # movemnt of the pawns
    def conditionalMovement(pos):
        if (307 <= pos[0] <= 307 + 10) and (410 <= pos[1] <= 410 + 10) and status:
            pos = [370, 420]
        elif (370 <= pos[0] <= 370 + 10) and (420 <= pos[1] <= 420 + 10):
            pos = [420, 420]
        elif (420 <= pos[0] <= 420 + 10) and (420 <= pos[1] <= 420 + 10):
            pos = [420, 370]

        # special edge case--1
        elif (420 <= pos[0] <= 420 + 10) and (370 <= pos[1] <= 370 + 10) and status:
            pos = [407, 310]
        elif (420 <= pos[0] <= 420 + 10) and (370 <= pos[1] <= 370 + 10) and not status:
            pos = [407, 330]

        elif (407 <= pos[0] <= 407 + 10) and (310 <= pos[1] <= 310 + 10) and status:
            pos = [420, 270]
        elif (407 <= pos[0] <= 407 + 10) and (330 <= pos[1] <= 330 + 10) and not status:
            pos = [420, 270]


        elif (420 <= pos[0] <= 420 + 10) and (270 <= pos[1] <= 270 + 10):
            pos = [420, 220]
        elif (420 <= pos[0] <= 420 + 10) and (220 <= pos[1] <= 220 + 10):
            pos = [370, 220]

        # special case --2
        elif (370 <= pos[0] <= 370 + 10) and (220 <= pos[1] <= 220 + 10) and status:
            pos = [307, 230]
        # end

        elif (307 <= pos[0] <= 307 + 10) and (230 <= pos[1] <= 230 + 10) and status:
            pos = [270, 220]
        elif (307 <= pos[0] <= 307 + 10) and (210 <= pos[1] <= 210 + 10) and not status:
            pos = [270, 220]
        elif (270 <= pos[0] <= 270 + 10) and (220 <= pos[1] <= 220 + 10):
            pos = [220, 220]
        elif (220 <= pos[0] <= 220 + 10) and (220 <= pos[1] <= 220 + 10):
            pos = [220, 270]

        # special case --3
        elif (220 <= pos[0] <= 220 + 10) and (270 <= pos[1] <= 270 + 10) and status:
            pos = [207, 310]
        elif (220 <= pos[0] <= 220 + 10) and (270 <= pos[1] <= 270 + 10) and not status:
            pos = [207, 330]

        elif (207 <= pos[0] <= 207 + 10) and (310 <= pos[1] <= 310 + 10) and status:
            pos = [220, 370]
        elif (207 <= pos[0] <= 207 + 10) and (330 <= pos[1] <= 330 + 10) and not status:
            pos = [220, 370]


        elif (220 <= pos[0] <= 220 + 10) and (370 <= pos[1] <= 370 + 10):
            pos = [220, 420]
        elif (220 <= pos[0] <= 220 + 10) and (420 <= pos[1] <= 420 + 10):
            pos = [270, 420]

        # specialcase--4
        elif (270 <= pos[0] <= 270 + 10) and (420 <= pos[1] <= 420 + 10) and not status:
            pos = [307, 430]
        elif (307 <= pos[0] <= 307 + 10) and (430 <= pos[1] <= 430 + 10) and not status:
            pos = [370, 420]

        # home special case--1
        elif (310 <= pos[0] <= 310 + 10) and (460 <= pos[1] <= 460 + 10):
            pos = [307, 410]
        elif (330 <= pos[0] <= 330 + 10) and (460 <= pos[1] <= 460 + 10):
            pos = [307, 410]
        elif (310 <= pos[0] <= 310 + 10) and (480 <= pos[1] <= 480 + 10):
            pos = [307, 410]
        elif (330 <= pos[0] <= 330 + 10) and (480 <= pos[1] <= 480):
            pos = [307, 410]

        # hone special case --2
        elif (310 <= pos[0] <= 310 + 10) and (160 <= pos[1] <= 160 + 10):
            pos = [307, 210]
        elif (330 <= pos[0] <= 330 + 10) and (160 <= pos[1] <= 160 + 10):
            pos = [307, 210]
        elif (310 <= pos[0] <= 310 + 10) and (180 <= pos[1] <= 180 + 10):
            pos = [307, 210]
        elif (330 <= pos[0] <= 330 + 10) and (180 <= pos[1] <= 180 + 10):
            pos = [307, 210]

        # for moving in conditions
        elif (270 <= pos[0] <= 270 + 10) and (420 <= pos[1] <= 420 + 10) and status and (counter_player_1 > 0):
            pos = [270, 370]
        elif (370 <= pos[0] <= 370 + 10) and (220 <= pos[1] <= 220 + 10) and not status and (counter_player_2 > 0):
            pos = [370, 270]

        # innerpath bottom to top
        elif (270 <= pos[0] <= 270 + 10) and (370 <= pos[1] <= 370 + 10):
            pos = [270, 320]
        elif (270 <= pos[0] <= 270 + 10) and (320 <= pos[1] <= 320 + 10):
            pos = [270, 270]
        elif (270 <= pos[0] <= 270 + 10) and (270 <= pos[1] <= 270 + 10):
            pos = [320, 270]

        # innerpath from
        elif (370 <= pos[0] <= 370 + 10) and (270 <= pos[1] <= 270 + 10):
            pos = [370, 320]
        elif (370 <= pos[0] <= 370 + 10) and (320 <= pos[1] <= 320 + 10):
            pos = [370, 370]
        elif (370 <= pos[0] <= 370 + 10) and (370 <= pos[1] <= 370 + 10):
            pos = [320, 370]

        # final position of player conditions
        # player one
        elif (320 <= pos[0] <= 320 + 10) and (370 <= pos[1] <= 370 + 10) and status:
            pos = [320, 330]
        elif (320 <= pos[0] <= 320 + 10) and (370 <= pos[1] <= 370 + 10) and not status:
            pos = [270, 370]

        # for player two
        elif (320 <= pos[0] <= 320) and (270 <= pos[1] <= 270 + 10) and not status:
            pos = [320, 310]
        elif (320 <= pos[0] <= 320) and (270 <= pos[1] <= 270 + 10) and status:
            pos = [370, 270]

        return pos

    # font for the letters and numbers
    font = pygame.font.Font('freesansbold.ttf', 20)

    # for printing the pawn values in safe cordinates
    def safeCorPlayerCount(player1_pos, player2_pos):
        spc1_pos = [[307, 410], [407, 310], [307, 230], [207, 310],[320,330]]
        spc1_counter = [0, 0, 0, 0,0]
        for i in player1_pos:
            if i == spc1_pos[0]:
                spc1_counter[0] += 1
            elif i == spc1_pos[1]:
                spc1_counter[1] += 1
            elif i == spc1_pos[2]:
                spc1_counter[2] += 1
            elif i == spc1_pos[3]:
                spc1_counter[3] += 1
            elif i==spc1_pos[4]:
                spc1_counter[4]+=1
        spc2_pos = [[307, 430], [407, 330], [307, 210], [207, 330],[320,310]]
        spc2_counter = [0, 0, 0, 0,0]
        for i in player2_pos:
            if i == spc2_pos[0]:
                spc2_counter[0] += 1
            elif i == spc2_pos[1]:
                spc2_counter[1] += 1
            elif i == spc2_pos[2]:
                spc2_counter[2] += 1
            elif i == spc2_pos[3]:
                spc2_counter[3] += 1
            elif i==spc2_pos[4]:
                spc2_counter[4]+=1
        return spc1_counter, spc2_counter

    def pawn_number(buffer1_cor, buffer2_cor):
        font1 = pygame.font.Font('freesansbold.ttf', 15)
        spc1_cor = ((327, 410), (420, 310), (327, 230), (227, 310),(330,330))
        spc2_cor = ((327, 430), (420, 330), (327, 210), (227, 330),(330,310))

        for i in range(5):
            if buffer1_cor[i] > 0:
                num1 = font1.render(str(buffer1_cor[i]), True, black)
                screen.blit(num1, spc1_cor[i])
            else:
                pass
        for j in range(5):
            if buffer2_cor[j] > 0:
                num1 = font1.render(str(buffer2_cor[j]), True, black)
                screen.blit(num1, spc2_cor[j])
            else:
                pass

    # to check if final pos is repeated
    def isPawnThere(pos):
        pawnIsThere = False
        if status:
            for i in player1_pos:
                if i == pos:
                    pawnIsThere = True
            return pawnIsThere
        else:
            for i in player2_pos:
                if i == pos:
                    pawnIsThere = True
            return pawnIsThere

    # if moved pawn is not in special condition
    def checkIfNotInSpeclCond(pos):
        spcl_cor_1 = [[307, 410], [407, 310], [307, 230], [207, 310],[320,330]]
        spcl_cor_2 = [[307, 430], [407, 330], [307, 210], [207, 330],[320,310]]
        spcl_status = False
        if status:
            for i in spcl_cor_1:
                if i == pos:
                    spcl_status = True
                    break
            return spcl_status
        else:
            for i in spcl_cor_2:
                if i == pos:
                    spcl_status = True
                    break
            return spcl_status

    def collision_1(x):
        collision_flag1 = None
        new = []

        for j in player2_pos:
            if j == x:
                # counter_player_1+=1
                collision_flag1 = True
                new = j

                break
        return collision_flag1, new

    def collision_2(y):
        collision_flag2 = None
        new = []
        for j in player1_pos:
            if j == y:
                collision_flag2 = True
                new = j

                break
        return collision_flag2, new

    eight_counter_1=0
    eight_counter_2=0


    # main while loop for game
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # mouse click values
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # text on button
        textSurf, textRect = text_object('Dice', font,(255,255,255))
        textRect.center = ((100 + (50 / 2)), (300 + (50 / 2)))

        # set the value to "to" variable

        if click == (1, 0, 0) and 100 <= mouse[0] <= 150 and 300 <= mouse[1] <= 350:
            to = random.choice(dice)
            status = not status
            time.sleep(.2)
            dicestatus = True
            # dice value to be printed

            #the working of 3 eigth's
            if status and to==8:
                eight_counter_1+=1
            elif status and to!=8:
                eight_counter_1=0
            elif not status and to==8:
                eight_counter_2+=1
            else:
                eight_counter_2=0
            if eight_counter_1==1:
                player1.set_pos(player1_pos)
            elif eight_counter_2==1:
                player2.set_pos(player2_pos)

            #setting the value of the dice color
            if status:
                player1.set_butn_status(True)
            else:
                player1.set_butn_status(False)
        print(to)
        #condition for getting initial position of pawns if three eight occurs
        if eight_counter_1==3:
            player1_pos=player1.get_pos()
            eight_counter_1=0
        #print(eight_counter_1,eight_counter_2)

        # player one movement
        elif status and not(eight_counter_1==3):
            if home_counter_1 == 4:
                if to == 8:
                    player1_pos[0] = [307, 410]
                    player1_pos[1] = [307, 410]
                    home_counter_1 -= 2
                    to -= to
                    status = not status
                    home_1[0] = False
                    home_1[1] = False
                elif to == 4:
                    player1_pos[0] = [307, 410]
                    home_counter_1 -= 1
                    to -= to
                    status = not status
                    home_1[0] = False
            elif home_counter_1 < 4:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(4):
                        if player1_pos[i][0] <= mouse[0] <= player1_pos[i][0] + 10 and player1_pos[i][1] <= mouse[1] <= \
                                player1_pos[i][1] + 10:
                            time.sleep(.25)
                            pos = player1_pos[i]
                            # function returns if home pawns is clicked
                            status_home_1, home_index_1 = ishomepawn(pos)
                            if (to == 4 or to == 8) and status_home_1:
                                if to == 4:
                                    player1_pos[i] = conditionalMovement(pos)
                                    to -= to
                                    status = not status
                                    home_1[home_index_1] = False
                                    home_counter_1 -= 1
                                elif to == 8:
                                    player1_pos[i] = conditionalMovement(pos)
                                    to -= 4
                                    home_1[home_index_1] = False
                                    home_counter_1 -= 1
                            elif not status_home_1:
                                buffer_1=[0,0]
                                temp_1=[0,0]
                                for n in range(to):
                                    pos = conditionalMovement(pos)
                                    temp_1=buffer_1
                                    buffer_1 = pos
                                if temp_1==pos:
                                    player1_pos[i]=player1_pos[i]
                                elif isPawnThere(pos):
                                    if checkIfNotInSpeclCond(pos):
                                        player1_pos[i] = pos
                                        if to == 4 or to == 8:
                                            status = not status
                                            to -= to
                                        else:
                                            to=-to
                                    else:
                                        player1_pos[i] = player1_pos[i]
                                else:
                                    player1_pos[i] = pos
                                    #to-=to#new alter

                                    yes1 = False
                                    if to == 4 or to == 8:
                                        status = not status
                                        to -= to
                                        yes1 = True
                                    else:
                                        to-=to

                                    status_collide, pos_y = collision_1(pos)
                                    if status_collide:
                                        counter_player_1 += 1
                                        player2_pos[player2_pos.index(pos_y)] = home_2_pos[player2_pos.index(pos_y)]
                                        home_counter_2 += 1
                                        if yes1:
                                            status = status
                                            to-=to
                                        else:
                                            status = not status
                                            to-=to

                            break

                            # new home condition

        #condition to get initial positions of player2 if three eight occurs
        elif eight_counter_2==3:
            player2_pos=player2.get_pos()
            eight_counter_2=0
        # player two movement
        elif status == False:
            #to move player1 from home position
            if home_counter_2 == 4:
                if to == 8:
                    player2_pos[0] = [307, 210]
                    player2_pos[1] = [307, 210]
                    home_counter_2 -= 2
                    status = not status
                    to -= to
                    # new changes
                    home_2[0] = False
                    home_2[1] = False
                elif to == 4:
                    player2_pos[0] = [307, 210]
                    home_counter_2 -= 1
                    status = not status
                    to -= to
                    # new changes
                    home_2[0] = False
            #to move the player after few player are moved from home
            elif home_counter_2 < 4:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(4):
                        if player2_pos[i][0] <= mouse[0] <= player2_pos[i][0] + 10 and player2_pos[i][1] <= mouse[1] <= \
                                player2_pos[i][1] + 10:
                            time.sleep(0.25)
                            pos = player2_pos[i]
                            status_home_2, home_index_2 = ishomepawn(pos)
                            if (to == 4 or to == 8) and status_home_2:
                                if to == 4:
                                    player2_pos[i] = conditionalMovement(pos)
                                    to -= to
                                    status = not status
                                    home_2[home_index_2] = False
                                    home_counter_2 -= 1
                                elif to == 8:
                                    player2_pos[i] = conditionalMovement(pos)
                                    to -= 4
                                    home_2[home_index_2] = False
                                    home_counter_2 -= 1
                            elif not status_home_2:
                                temp_2 = [0, 0]
                                buffer_2 = [0, 0]
                                for n in range(to):
                                    pos = conditionalMovement(pos)
                                    temp_2=buffer_2
                                    buffer_2=pos
                                if temp_2==pos:
                                    player2_pos[i]=player2_pos[i]
                                elif isPawnThere(pos):
                                    if checkIfNotInSpeclCond(pos):
                                        player2_pos[i] = pos
                                        if to == 4 or to == 8:
                                            to -= to
                                            status = not status
                                    else:
                                        player2_pos[i] = player2_pos[i]
                                else:
                                    player2_pos[i] = pos
                                    #to-=to
                                    yes2 = False
                                    if to == 4 or to == 8:
                                        to -= to
                                        status = not status
                                        yes2 = True
                                    else:
                                        to-=to
                                    status_collide2, pos_x = collision_2(pos)

                                    if status_collide2:
                                        counter_player_2 += 1
                                        player1_pos[player1_pos.index(pos_x)] = home_1_pos[player1_pos.index(pos_x)]
                                        home_counter_1 += 1
                                        if yes2:
                                            status = status
                                            to-=to
                                        else:
                                            status = not status
                                            to-=to

                            break


        # place every thing that needs to be printed printed
        screen.fill((217, 223, 185))

        # to print the board
        board()

        # print the number of player one and two
        buffer1_cor, buffer2_cor = safeCorPlayerCount(player1_pos, player2_pos)
        pawn_number(buffer1_cor, buffer2_cor)

        # for placing the player 1 at the cordinates
        for i in range(4):
            if enable1[i]:
                player1.draw(player1_pos[i])

        # for placing the plauer 2 at the cordinates
        for i in range(4):
            if enable2[i]:
                player2.draw(player2_pos[i])

        # dice button
        pygame.draw.rect(screen, (0, 0, 0), (100, 300, 50, 50))
        # turn grey if hover on the dice button
        if (100 < mouse[0] < 150) and (300 < mouse[1] < 350):
            pygame.draw.rect(screen, (105, 105, 105), (100, 300, 50, 50))
        # color of the dice panel
        dicepanel, dicerect = text_object(str(to), font, (255, 255, 255))
        dicerect.center = ((100 + (50 / 2)), (400 + (50 / 2)))
        if player1.get_butn_status():
            pygame.draw.rect(screen, cyan, (100, 400, 50, 50))
        elif not player2.get_butn_status():
            pygame.draw.rect(screen, yellow, (100, 400, 50, 50))

        # text on Dice
        screen.blit(textSurf, textRect)
        if dicestatus:
            screen.blit(dicepanel, dicerect)
        pygame.display.update()
        # end of the printing place
        # game fps--curretly at 30
        clock.tick(30)
gameintro()
gameEngine()
