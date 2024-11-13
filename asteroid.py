import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        asteroid_angle = random.uniform(20, 50)
        vec_1 = self.velocity.rotate(asteroid_angle)
        vec_2 = self.velocity.rotate(-asteroid_angle)

        smaller_radius = self.radius - ASTEROID_MIN_RADIUS

        smaller_asteroid_1 = Asteroid(
            self.position.x, self.position.y, smaller_radius)
        smaller_asteroid_2 = Asteroid(
            self.position.x, self.position.y, smaller_radius)

        smaller_asteroid_1.velocity = vec_1 * ASTEROID_INCREASE_SPEED
        smaller_asteroid_2.velocity = vec_2 * ASTEROID_INCREASE_SPEED
