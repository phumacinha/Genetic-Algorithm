from __future__ import annotations
from random import randint
from typing import List
import numpy as np


class Chromosome(object):
    def __init__(self, num_of_genes: int, value):
        self.num_of_genes = num_of_genes
        self.value = value

    def __repr__(self):
        return str(self.as_int())

    def as_int(self):
        value_as_list = self.value.tolist()
        factor = -1 if value_as_list[0] == 1 else 1

        value_as_bin = ''.join(map(str, value_as_list[1:]))

        return factor*int(value_as_bin, base=2)

    def crossover(self, another_chromo:Chromosome) -> List[Chromosome]:
        crossover_point = randint(0, self.num_of_genes - 1)

        children = [
            np.concatenate((self.value[:crossover_point], another_chromo.value[crossover_point:])),
            np.concatenate((another_chromo.value[:crossover_point], self.value[crossover_point:]))
        ]

        generate_child = lambda value: Chromosome(self.num_of_genes, value)
        return list(map(generate_child, children))

    def mutate(self) -> Chromosome:
        selected_bit = randint(0, self.num_of_genes - 1)
        self.value[selected_bit] = (self.value[selected_bit] + 1) % 2

        return self

    def set_value(self, value: int):
        abs_value_as_bin = bin(abs(value))[2:].rjust(4, '0')
        signed = '1' if value < 0 else '0'
        value_as_bin = signed + abs_value_as_bin

        self.value = np.array(list(value_as_bin), dtype=int)

    def random(num_of_genes:int) -> Chromosome:
        value = np.random.randint(0, 2, num_of_genes) 
        return Chromosome(num_of_genes, value)