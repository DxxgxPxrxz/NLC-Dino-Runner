#EL ARCHIVO GAME ES LA ESTRUCTURA CENTRAL DEL JUEGO, ES LA COLUMNA VERTEBRAL EN EL QUE ENCAJAN TODOS LOS COMPONENTES

import pygame #Esta es la libreria principal para el programa, es utilizada frecuentemente en otros files

#Importando del folder components:
from nlc_dino_runner.components.lives.lives import Live
from nlc_dino_runner.components.lives.livesManager import LiveManager
from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.components.dinosaur import Dinosaur #Importando una class desde un Python File proveniente de la carpeta COMPONENTS (en este caso la class llamada "Dinosaur")
from nlc_dino_runner.components.obstacles.obstaclesManager import ObstaclesManager# //
from nlc_dino_runner.utils.constants import RUNNING, TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, GAME_THEME, \
    DARK_MODE, NORMAL_MODE, CLOUD  # Importando constantes #AÑADIDO



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_pos_bg = 0
        self.lives = Live()
        self.y_pos_bg = 380
        self.game_speed = 30
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.live = Live()
        self.live_manager = LiveManager()
        self.points = 0
        self.running = True
        self.death_count = 0

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)
        self.live_manager.reset_lives()
        self.game_speed = 30
        self.points = 0
        self.playing = True
        GAME_THEME.play()#AÑADIDO
        while self.playing:
            self.event()
            self.update()
            self.draw()
        #pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self, self.screen)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.score()
        self.draw_background()
        self.draw_sky()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.live_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        if (self.points // 1000) % 2 == 1:
            self.screen.fill(DARK_MODE)
        else:
            self.screen.fill(NORMAL_MODE)

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invincibility(self.screen)
        #self.player.check_hammer(self.screen)

    def draw_background(self):

        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))

        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_sky(self):

        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_bg + 1100, self.y_pos_bg - 200))
        self.screen.blit(CLOUD, (self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg > +image_width:
            self.screen.blit(CLOUD, (self.x_pos_bg + 1100, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg += self.game_speed - 30

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()
                GAME_THEME.stop()#AÑADIDO

    def show_menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)


        #futuramente vamos a mostrar el menu
        self.print_menu_elements()

        pygame.display.update()

        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):

        half_screen_height = SCREEN_HEIGHT // 2
        death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count), height=half_screen_height + 50)
        points, points_rect = text_utils.get_centered_message("Your score: " + str(self.points), height=half_screen_height + 100)

        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message('Press any key to Start')

        else:
            text, text_rect = text_utils.get_centered_message('Press any key to Restart')

        self.screen.blit(ICON, ((SCREEN_WIDTH // 2) - 40, (half_screen_height - 150)))

        self.screen.blit(text, text_rect)
        self.screen.blit(death_score, death_score_rect)
        self.screen.blit(points, points_rect)
        self.screen.blit(points, points_rect)


