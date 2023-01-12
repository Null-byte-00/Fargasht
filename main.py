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
from interface import Simulation

pygame.init()

BACKGROUND_COLOR = (70,70,255)
CANVAS_SIZE = [800,800]

canvas = pygame.display.set_mode(CANVAS_SIZE)

pygame.display.set_caption("Fargasht")

canvas.fill(BACKGROUND_COLOR)

sim = Simulation(canvas, 100, CANVAS_SIZE, surface_color=BACKGROUND_COLOR, plankton_size=10, speed=1.5, internal_num=10, generation_period=300,generation_num=300)

sim.run()

