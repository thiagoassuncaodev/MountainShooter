import random
from code.background import Background
from code.const import WIN_WIDTH,WIN_HEIGHT
from code.player import player
from code.enemy import Enemy


class EntityFactory:
    
    
    @staticmethod
    def get_entity(entity_name:str, position = (0,0)):

        match entity_name:
            case 'Level1bg':
                list_bg =[]
                for i in range(7):
                    list_bg.append(Background(f'Level1bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1bg{i}',(WIN_WIDTH,0)))
                return list_bg
            case 'Level2bg':
                list_bg =[]
                for i in range(5):
                    list_bg.append(Background(f'Level2bg{i}',(0,0)))
                    list_bg.append(Background(f'Level2bg{i}',(WIN_WIDTH,0)))
                return list_bg
            case 'player1':
                return player('player1',(10,WIN_HEIGHT / 2 - 30))
            case 'player2':
                return player('player2',(10,WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT -40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT - 40)))