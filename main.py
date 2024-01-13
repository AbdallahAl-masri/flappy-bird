from sys import exit
import random
from settings import *
from pygame.sprite import Sprite
from ground import Ground
from bird import Bird
from pygame import mixer

pygame.init()

# Controls Frame Rate
clock = pygame.time.Clock()
score = 0
# Caption
pygame.display.set_caption('Wing Jump Game')

# Icon Picture
icon = pygame.image.load('images/icon.jfif')
pygame.display.set_icon(icon)

# Background Sound
mixer.music.load('sounds/Flappy Bird Theme Song.mp3')
mixer.music.play(-1)

class Pipe(Sprite):
    def __init__(self, x, y, image, pipe_type, window):
        super(Pipe, self).__init__()
        self.window = window
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type

    def update(self):
        # Move Pipe
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()

        # Score
        global score
        if self.pipe_type == 'bottom':
            if bird_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if bird_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                score += 1

        # Show Score
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        self.window.blit(score_text, (20, 20))




# Window
window = pygame.display.set_mode((win_width, win_height))
def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Game Main Method
def main():


    # Instantiate Bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())

    # Setup Pipes
    pipe_timer = 0
    pipes = pygame.sprite.Group()

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))

    run = True
    while run:
        global score
        # Quit
        quit_game()

        # User Input
        user_input = pygame.key.get_pressed()

        # Draw Background
        window.blit(skyline_image, (0, 0))

        # Spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground))

        # Draw - Pipes, Ground and Bird
        pipes.draw(window)
        ground.draw(window)
        bird.draw(window)

        # Update - Pipes, Ground and Bird
        if bird.sprite.alive:
            pipes.update()
            ground.update()
        bird.update(user_input)

        # Collision Detection
        collision_pipes = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
        collision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
        if collision_pipes or collision_ground:
            bird.sprite.alive = False
            if collision_ground or collision_pipes:
                window.blit(game_over_image, (win_width // 2 - game_over_image.get_width() // 2,
                                              win_height // 2 - game_over_image.get_height() // 2))
                score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
                window.blit(score_text, ((win_width + 100) // 2 - game_over_image.get_width()  // 2,
                                              (win_height - 50) // 2 - game_over_image.get_height()  // 2))
                if user_input[pygame.K_r]:
                    score = 0
                    break

        # Spawn Pipes
        if pipe_timer <= 0 and bird.sprite.alive:
            x_top, x_bottom = 799, 799
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + bottom_pipe_image.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_image, 'top', window))
            pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image, 'bottom', window))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1

        clock.tick(55)
        pygame.display.update()

# Menu
def menu():
    global game_stopped

    while game_stopped:
        quit_game()

        # Draw Menu
        window.fill((0, 0, 0))
        window.blit(skyline_image, (0, 0))
        window.blit(ground_image, Ground(0, 520))
        window.blit(bird_images[0], (100, 250))
        start = font.render('Press Space to Start', True, pygame.Color(255, 255, 255))
        window.blit(start, (win_width // 2 , win_height // 2 ))

        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()

menu()
