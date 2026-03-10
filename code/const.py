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
    'player1Shot': 1,
    'player2': 3,
    'player2Shot': 3,
    'Enemy1':1,
    'Enemy1Shot':5,
    'Enemy2':1,
    'Enemy2Shot':2,
}

ENTITY_HEALTH = {
    'Level1bg0': 999,
    'Level1bg1': 999,
    'Level1bg2': 999,
    'Level1bg3': 999,
    'Level1bg4': 999,
    'Level1bg5': 999,
    'Level1bg6': 999,
    'player1': 300,
    'player1Shot': 1,
    'player2': 300,
    'player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}
ENTITY_SHOT_DELAY = {
    'player1': 20,
    'player2': 15,
    'Enemy1':100,
    'Enemy2':200,

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