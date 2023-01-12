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
import math, random
import numpy as np
from brain import Brain
from planktons import PlanktonGraphics
import pygame

class Plankton:
    """
    An interface between brain and graphics
    """
    def __init__(self, surfce, pos_x=100, pos_y=100, others =np.array([]), size=20, surface_size=[1000,1000], surface_color=(0,0,0),speed=5,
    inernal_num=5) -> None:
        """
        others: 2d array that shows the position of other planktons
        [[x,y,size]
        ,[x,y,size]
        ...]
        """
        self.brain = Brain(9, inernal_num, 8)
        self.graphics = PlanktonGraphics(surfce, pos_x, pos_y, size, self.get_color(), surface_size, surface_color, speed)
        self.others = others
        self.age = 0

    def get_color(self):
        """
        makes an rgb color according to creture's genetics
        """
        gnome = self.brain.export_gnome()
        return (gnome[3], gnome[4], gnome[5])
    
    def can_move(self, x,y):
        """
        Checks if the creature can move to a position without any collisions 
        """

        for another_plankton in self.others:
            if math.sqrt(((x - another_plankton[0])**2) + ((y - another_plankton[1])**2)) < ((self.graphics.size + another_plankton[2]) / 2):
                return False
        
        if not (0 < x < self.graphics.surface_size[0] and 0 < y < self.graphics.surface_size[1]):
            return False
        
        return True

    # Output(action) methods

    def move_right(self):
        """
        0: moves the object one step right
        """
        if self.can_move(self.graphics.X + self.graphics.speed, self.graphics.Y):
            self.graphics.move_right()

    def move_left(self):
        """
        1: moves the object one step left
        """
        if self.can_move(self.graphics.X - self.graphics.speed, self.graphics.Y):
            self.graphics.move_left()
    
    def move_up(self):
        """
        2: moves the object one step up
        """
        if self.can_move(self.graphics.X, self.graphics.Y - self.graphics.speed):
            self.graphics.move_up()
    
    def move_down(self):
        """
        3: moves the object one step up
        """
        if self.can_move(self.graphics.X, self.graphics.Y - self.graphics.speed):
            self.graphics.move_down()
    
    def move_upright(self):
        """
        4: moves the object one step upright
        """
        if self.can_move(self.graphics.X + self.graphics.speed, self.graphics.Y + self.graphics.speed):
            self.graphics.move_up()
            self.graphics.move_right()
    
    def move_downright(self):
        """
        5: moves the object one step downright
        """
        if self.can_move(self.graphics.X + self.graphics.speed, self.graphics.Y + self.graphics.speed):
            self.graphics.move_down()
            self.graphics.move_right()
    
    def move_upleft(self):
        """
        6: moves the object one step upleft
        """
        if self.can_move(self.graphics.X + self.graphics.speed, self.graphics.Y + self.graphics.speed):
            self.graphics.move_up()
            self.graphics.move_left()
    
    def move_downleft(self):
        """
        7: moves the object one step downleft
        """
        if self.can_move(self.graphics.X + self.graphics.speed, self.graphics.Y + self.graphics.speed):
            self.graphics.move_down()
            self.graphics.move_left()
    
    #Input methods

    def get_x(self):
        """
        0: return the x axis of creature
        """
        return self.graphics.X
    
    def get_y(self):
        """
        1: returns the y axis of creature
        """
        return self.graphics.Y
    
    def get_population(self):
        """
        2: returns the population of planktons
        """
        return len(self.others)
    
    def oscillator(self):
        """
        3: returns the value of oscillator function
        """
        return math.sin(self.age / 5) * 100
    
    def get_age(self):
        """
        4: returns the age of creature
        """
        return self.age
    
    def random_value(self):
        """
        5: returns a random number
        """
        return random.uniform(-100, 100)

    def get_nearest_plankton_dist(self):
        """
        6: returns the nearest plankton's distance
        """
        nearest_dist = 10000
        for another_plankton in self.others:
            dist = (math.sqrt(((self.graphics.X - another_plankton[0])**2) + ((self.graphics.Y - another_plankton[1]) ** 2))) - self.graphics.size - another_plankton[2]
            if nearest_dist > dist:
                nearest_dist = dist
        return nearest_dist
    
    def get_rightborder_dist(self):
        """
        7: returns distance from left border
        """
        return (self.graphics.surface_size[0] - self.graphics.X)

    def get_downborder_dist(self):
        """
        8: returns the distance from down border
        """
        return (self.graphics.surface_size[1] - self.graphics.Y)

    def update(self):
        self.graphics.color = self.get_color()
        outputs = self.brain.run([
            self.get_x(),
            self.get_y(),
            self.get_population(),
            self.oscillator(),
            self.get_age(),
            self.random_value(),
            self.get_nearest_plankton_dist(),
            self.get_rightborder_dist(),
            self.get_downborder_dist(),
            ]) 

        result = outputs > 0

        if result[0]:
            self.move_right()
        if result[1]:
            self.move_left()
        if result[2]:
            self.move_up()
        if result[3]:
            self.move_down()
        if result[4]:
            self.move_upright()
        if result[5]:
            self.move_downright()
        if result[6]:
            self.move_upleft()
        if result[7]:
            self.move_downleft()
        
        self.age += 1
        self.graphics.draw()
    


class Simulation:
    def __init__(self,surface, plankton_num=100, surface_size=[1000, 800], plankton_size=20, surface_color=(0,0,0), speed=1, internal_num=5,
    generation_period=1000, generation_num=100) -> None:
        """
        creating generation 0 with random brain connections
        """
        self.plankton_num = plankton_num
        self.surface_size = surface_size
        self.plankton_size = plankton_size
        self.internal_num = internal_num
        self.surface_color = surface_color
        self.speed= speed
        self.surface = surface
        self.generation_period = generation_period
        self.generation_num = generation_num
        self.generation = 0
        self.planktons = []
        self.positions = np.array([])
        for i in range(self.plankton_num):
            random_x = random.randint(0, surface_size[0] - 1)
            random_y = random.randint(0, surface_size[1] - 1)
            self.planktons.append(Plankton(self.surface, others=np.array([[2000,2000,1]]), surface_size=surface_size, pos_x=random_x, pos_y=random_y, 
            surface_color=surface_color, size=plankton_size, speed=speed, inernal_num=internal_num))
        self.update_others_list()
    
    def update_others_list(self):
        """
        As each plankton has an 'others' field, this method tells each plankton where other planktons are
        """
        i = 0
        other_planktons = self.planktons
        for plankton in self.planktons:
            self.planktons[i].others = np.array([[2000,2000,self.plankton_size]])
            for another_plankton in other_planktons:
                if plankton != another_plankton:
                    self.planktons[i].others = np.concatenate([plankton.others, [[another_plankton.graphics.X, another_plankton.graphics.Y, another_plankton.graphics.size]]], axis=0)
            if plankton.others[0].tolist() == [2000,2000,self.plankton_size]:
                self.planktons[i].others = np.delete(plankton.others, 0, axis=0)
            i +=1

    
    def run(self):
        """
        starts the simulation
        """
        for generation in range(self.generation_num):
            for smth in range(self.generation_period):
                for plankton in self.planktons:
                    plankton.update()
                self.update_others_list()
                pygame.display.update()
            i = 0
            for plankton in self.planktons:
                if plankton.graphics.X < 750:
                    self.planktons.pop(i)
                i += 1
            # create the next genertion
            previous_planktons = self.planktons
            print(f"Generation: {generation + 1}, Survivors: {len(previous_planktons)}" )
            self.planktons = []

            for smth in range(self.plankton_num):
                random_x = random.randint(0, self.surface_size[0] - 1)
                random_y = random.randint(0, self.surface_size[1] - 1)
                self.planktons.append(Plankton(self.surface, others=np.array([[2000,2000,1]]), surface_size=self.surface_size, pos_x=random_x, pos_y=random_y, 
                surface_color=self.surface_color, size=self.plankton_size, speed=self.speed, inernal_num=self.internal_num))

            j = 0
            for smth in range(self.plankton_num):
                parent_1 = previous_planktons[random.randint(0, len(previous_planktons) - 1)] 
                parent_2 = previous_planktons[random.randint(0, len(previous_planktons) - 1)] 
                self.planktons[j].brain.combine_gnomes(parent_1.brain.export_gnome(), parent_2.brain.export_gnome())
                j += 1
            
            self.update_others_list()
            self.surface.fill(self.surface_color)
            self.generation += 1
            pygame.display.set_caption("Generation: " + str(self.generation))

        self.update_others_list()