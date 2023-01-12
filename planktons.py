"""
    Fargasht, a simple evolution simulator. Github: https://github.com/Null-byte-00/
    Copyright (C) 2022  Soroush(Amirali) Rfie

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import pygame

class PlanktonGraphics:
    """
    Class to display a plankton using pygame
    """
    def __init__(self, surfce, pos_x=100, pos_y=100, size=20, color=(200,0,0), surface_size=[1000,1000], surface_color=(0,0,0),speed=5) -> None:
        """
        surface: pygame surface
        position: initial position of plankton
        size: size of plankton
        color: plankton's color
        surface_color, surface_size: size and color of the surface
        speed: object's speed
        """
        self.surface = surfce
        self.X = pos_x
        self.Y = pos_y
        self.size = size
        self.color = color
        self.surface_size = surface_size
        self.surface_color = surface_color
        self.speed = speed
    
    def draw(self):
        """
        draws plankton on the surface
        """
        # drawing the center
        pygame.draw.circle(self.surface, self.color,(self.X, self.Y) , self.size / 2)
        pygame.draw.circle(self.surface, (255,255,255), (self.X, self.Y), self.size / 3)
        pygame.draw.circle(self.surface, (0,0,0), (self.X, self.Y), self.size / 4)
    
    def clear(self):
        """
        removes object  from surface
        """
        pygame.draw.circle(self.surface, self.surface_color, (self.X, self.Y), self.size / 2)

    def move_right(self):
        """
        moves the object right
        """
        self.clear()
        self.X += self.speed
        self.draw()

    def move_left(self):
        """
        moves the object left
        """
        self.clear()
        self.X -= self.speed
        self.draw()
    
    def move_up(self):
        """
        moves the object up
        """
        self.clear()
        self.Y -= self.speed
        self.draw()
    
    def move_down(self):
        """
        moves the object up
        """
        self.clear()
        self.Y += self.speed
        self.draw()

    