from __future__ import annotations
from random import randint, random
from typing import List
import numpy as np


class Chromosome(object):
    def __init__(self, num_of_genes: int, value):
        self.num_of_genes = num_of_genes
        self.value = value
        self.is_alive = True

    def __repr__(self):
        return str(self.as_int())

    def as_int(self):
        value_as_list = self.value.tolist()
        factor = -1 if value_as_list[0] == 1 else 1

        value_as_bin = ''.join(map(str, value_as_list[1:]))

        return factor*int(value_as_bin, base=2)

    def crossover(self, another_chromo:Chromosome) -> List[Chromosome]:
        crossover_point = randint(0, self.num_of_genes - 1)
        print('crossover_point', crossover_point)

        children = [
            np.concatenate((self.value[:crossover_point], another_chromo.value[crossover_point:])),
            np.concatenate((another_chromo.value[:crossover_point], self.value[crossover_point:]))
        ]

        generate_child = lambda value: Chromosome(self.num_of_genes, value)
        return list(map(generate_child, children))

    def mutate(self) -> Chromosome:
        selected_bit = randint(0, self.num_of_genes - 1)
        self.value[selected_bit] = (self.value[selected_bit] + 1) % 2
        print(f'mutação do bit #{selected_bit}')

        return self

    def random(num_of_genes:int) -> Chromosome:
        value = np.random.randint(0, 2, num_of_genes) 
        return Chromosome(num_of_genes, value)

    def kill(self):
        self.is_alive = False

chromo1 = Chromosome.random(num_of_genes = 5)
chromo2 = Chromosome.random(num_of_genes = 5)
print('chromo1', chromo1, chromo1.value)
print('chromo2', chromo2, chromo2.value)

print()
filho1, filho2 = chromo1.crossover(chromo2)
print()
print('filho1', filho1, filho1.value)
print('filho1 após mutação', filho1.mutate(), filho1.value)
print()

print('filho2', filho2, filho2.value)
print('filho2 após mutação', filho2.mutate(), filho2.value)