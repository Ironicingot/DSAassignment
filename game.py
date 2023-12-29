import pygame
import random


class Game:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed

    def move(self, WIDTH, HEIGHT, CAR_WIDTH):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0 - self.image.get_height()
            self.x = random.randint(0, WIDTH - CAR_WIDTH)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collides(self, other_game_instance):
        return (self.x < other_game_instance.x + other_game_instance.image.get_width() and
                self.x + self.image.get_width() > other_game_instance.x and
                self.y < other_game_instance.y + other_game_instance.image.get_height() and
                self.y + self.image.get_height() > other_game_instance.y)


class GameEngine:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 800, 600
        self.CAR_WIDTH = 50
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Car Dodger")
        self.clock = pygame.time.Clock()

        self.player_car_image = GameEngine.load_and_scale_image("player_car.png", self.CAR_WIDTH)
        self.enemy_car_image = GameEngine.load_and_scale_image("enemy_car.png", self.CAR_WIDTH)
        self.background_image = GameEngine.load_and_scale_image("highway_background.png", self.WIDTH)

        self.level = 1

        self.player = Game(self.WIDTH // 2, self.HEIGHT - 2 * self.player_car_image.get_height(), self.player_car_image, 0)
        self.enemy_instances = [Game(random.randint(0, self.WIDTH - self.CAR_WIDTH), i * -self.enemy_car_image.get_height(), self.enemy_car_image, 5) for i in range(5)]

    @staticmethod
    def load_and_scale_image(filename, base_width):
        img = pygame.image.load(filename)
        w_percent = base_width / float(img.get_rect().size[0])
        h_size = int((float(img.get_rect().size[1]) * float(w_percent)))
        return pygame.transform.scale(img, (base_width, h_size))

    def run(self):
        points = 0
        font = pygame.font.SysFont('Brush Script MT', 35)
        level_message_timer = 0
        points_increment = 10
        running = True
        last_points_update = pygame.time.get_ticks()

        while running:
            self.screen.blit(self.background_image, (0, 0))
            current_time = pygame.time.get_ticks()
            time_interval = max(50, 2000 - self.level * 50)

            if current_time - last_points_update >= time_interval:
                adjusted_points_increment = points_increment * (1 + 0.03 * (self.level - 1))
                points += adjusted_points_increment
                last_points_update = current_time

            if points >= self.level * 100:
                self.level += 1
                level_message_timer = 120
                for enemy in self.enemy_instances:
                    enemy.speed += 1

            if level_message_timer > 0:
                level_label = font.render(f"Reached Level {self.level}!", True, (255, 0, 0))
                self.screen.blit(level_label, (self.WIDTH // 2 - level_label.get_width() // 2, self.HEIGHT // 2 - level_label.get_height() // 2))
                level_message_timer -= 1

            points_label = font.render(f"Points: {int(points)}", True, (0, 0, 0))
            self.screen.blit(points_label, (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.player.y > 0:
                self.player.y -= 5
            if keys[pygame.K_DOWN] and self.player.y < self.HEIGHT - self.player_car_image.get_height():
                self.player.y += 5
            if keys[pygame.K_LEFT] and self.player.x > 0:
                self.player.x -= 5
            if keys[pygame.K_RIGHT] and self.player.x < self.WIDTH - self.CAR_WIDTH:
                self.player.x += 5

            for enemy in self.enemy_instances:
                enemy.move(self.WIDTH, self.HEIGHT, self.CAR_WIDTH)
                enemy.draw(self.screen)
                if self.player.collides(enemy):
                    running = False

            self.player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


game_instance = GameEngine()
game_instance.run()
