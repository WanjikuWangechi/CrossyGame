import pygame
from gameobject import GameObject
from player import Player


class Game:
    def __init__(self) :


        self.width = 800
        self.height = 800
        self.white_colour = (255, 255, 255)

        #Game Code
        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        
        self.background = GameObject(0, 0, self.width, self.height, 'assets/background.png')

        self.treasure = GameObject(370 , 50, 50, 50, 'assets/treasure.png')

        self.player = Player(370, 700, 50, 50, 'assets/player.png', 10 )
        

    

    def draw_objects(self):

            
        self.game_window.fill(self.white_colour)

        self.game_window.blit(self.background.image, (self.background.x, self.background.y))

        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))

        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        pygame.display.update()



    def run_game_loop(self):

        player_direction = 0

        while True:
            #handle events
            pygame.event.get()
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.quit:
                    return
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                        #MOVE PLAYER UP
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                        #MOVE PLAYER DOWN


            #execute logic

            self.player.move(player_direction)
            #update display
            self.draw_objects()



            self.clock.tick(60)
