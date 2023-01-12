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
import numpy as np
import random

class Brain:
    """
    Plankton's Brain.
    A simple one layer neural network 
    """
    def __init__(self, input_num: int, internal_num: int, output_num: int) -> None:
        """
        input_num: the number of input nodes(neurons)
        internal_num: the number of internal nodes(neurons)
        output_num: the number of internal nodes(neurons)
        """
        self.input_num = input_num
        self.internal_num = internal_num
        self.output_num = output_num
        self.create_weights()
    
    def create_weights(self):
        """
        Creates weight matrices
        """
        # Matrix for connection between input and internal nodes
        self.in_int_weights = np.random.uniform(-4,4,[self.internal_num, self.input_num])
        # Matrix for connections between internal and output neurons
        self.int_out_weights = np.random.uniform(-4,4,[self.output_num, self.internal_num])
    
    def activation(self, matrix):
        """
        activation function
        """
        return np.tanh(matrix)
    
    def run(self, input_array):
        """
        runs network and returns outputs
        """
        if len(input_array) != self.input_num:
            raise Exception("the input array size doesn't match the number of inputs")
        input_column = np.array(input_array, ndmin=2).T
        internal_output = self.activation(self.in_int_weights @ input_column)
        output_array = self.activation(self.int_out_weights @ internal_output)
        return output_array
    
    def export_gnome(self) -> bytes:
        """
        Imports connection in form of a string
        format:(x-axis)(y-axis)(input to internal array bytes)\xff\xfd\xfd\xff(x-axis)(y-axis)(internal to output array bytes)
        """
        in_ints_shape = bytes(self.in_int_weights.shape)
        in_int_bytes = self.in_int_weights.tobytes()

        int_out_shape = bytes(self.int_out_weights.shape)
        int_out_bytes = self.int_out_weights.tobytes()

        gnome = in_ints_shape + in_int_bytes + b'\xff\xfd\xfd\xff' + int_out_shape + int_out_bytes
        return gnome
    
    def import_gnome(self, gnome: bytes):
        """
        import weight arrays from a gnome
        """
        in_ints_combined = gnome.split(b'\xff\xfd\xfd\xff')[0]
        int_out_combined = gnome.split(b'\xff\xfd\xfd\xff')[1]

        in_int_array = np.frombuffer(in_ints_combined[2:], dtype='float').reshape([in_ints_combined[0], in_ints_combined[1]])
        int_out_array = np.frombuffer(int_out_combined[2:], dtype='float').reshape([int_out_combined[0], int_out_combined[1]])

        self.in_int_weights = in_int_array
        self.int_out_weights = int_out_array
    
    @staticmethod
    def mix_arrays(array_1: np.ndarray, array_2: np.ndarray):
        """
        randomly mixes two arrays
        """
        if not array_1.shape == array_2.shape:
            raise Exception("Two input arrays have different shapes")
        #choice = np.random.randint(2, size = X.size).reshape(X.shape).astype(bool)
        choice = np.random.randint(2,size=array_1.size).reshape(array_1.shape).astype(bool)
        return np.where(choice, array_1, array_2)
    
    @staticmethod
    def add_random_array(a: np.ndarray, mutation_rate: int):
        """
        Adds a random number to array if a mutation happens
        """
        oned_a = None
        if random.uniform(0,1) <= mutation_rate:
            oned_a = a.reshape([1, a.size])
            oned_a[0,np.random.randint(0, oned_a.size - 1)] = np.random.uniform(-4,4)
            return oned_a.reshape(a.shape)
        else:
            return a

    def combine_gnomes(self,gnome_1, gnome_2, mutation_rate=0.01):
        """
        Mixes two given gnomes with choosing values from each of them(a simulation of mating in nature)
        mutation_rate: defines the probability of a mutation which causes the creature to have a neuron connection 
        which it didn't inherit from its parents (mutation_rate=0.01 means mutations happen 5 in 100s times)
        """
        in_ints_combined = gnome_1.split(b'\xff\xfd\xfd\xff')[0]
        int_out_combined = gnome_1.split(b'\xff\xfd\xfd\xff')[1]

        in_int_array_1 = np.frombuffer(in_ints_combined[2:], dtype='float').reshape([in_ints_combined[0], in_ints_combined[1]])
        int_out_array_1 = np.frombuffer(int_out_combined[2:], dtype='float').reshape([int_out_combined[0], int_out_combined[1]])

        in_ints_combined = gnome_2.split(b'\xff\xfd\xfd\xff')[0]
        int_out_combined = gnome_2.split(b'\xff\xfd\xfd\xff')[1]

        in_int_array_2 = np.frombuffer(in_ints_combined[2:], dtype='float').reshape([in_ints_combined[0], in_ints_combined[1]])
        int_out_array_2 = np.frombuffer(int_out_combined[2:], dtype='float').reshape([int_out_combined[0], int_out_combined[1]])

        self.in_int_weights = Brain.add_random_array(Brain.mix_arrays(in_int_array_1, in_int_array_2), mutation_rate)
        self.int_out_weights = Brain.add_random_array(Brain.mix_arrays(int_out_array_1, int_out_array_2), mutation_rate)


