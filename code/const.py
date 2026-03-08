import pygame
#C
COLOR_ORANGE = (255,128,0)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED ={
    'Level1bg0': 0,
    'Level1bg1':1,
    'Level1bg2':2,
    'Level1bg3':3,
    'Level1bg4':4,
    'Level1bg5':5,
    'Level1bg6':6,
    'player1': 3,
    'player2': 3,
    'Enemy1':2,
    'Enemy2':1,
}



#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
#P
PLAYER_KEY_UP = {'player1': pygame.K_UP,
                 'player2': pygame.K_w}
PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN,
                   'player2': pygame.K_s}
PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT,
                   'player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT,
                    'player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'player1': pygame.K_RCTRL,
                    'player2': pygame.K_LCTRL}

#S
SPAWN_TIME = 4000
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324