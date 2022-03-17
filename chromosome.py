from __future__ import annotations
from random import randint
from typing import List
import numpy as np


class Chromosome(object):
    def __init__(self, num_of_genes: int, genes):
        self.num_of_genes = num_of_genes
        self.genes = genes

    def __repr__(self):
        return str(self.as_int())

    def as_int(self):
        value_as_list = self.genes.tolist()
        factor = -1 if value_as_list[0] == 1 else 1

        value_as_bin = ''.join(map(str, value_as_list[1:]))

        return factor*int(value_as_bin, base=2)

    def crossover(self, another_chromo:Chromosome) -> List[Chromosome]:
        crossover_point = randint(0, self.num_of_genes - 1)

        children = [
            np.concatenate((self.genes[:crossover_point], another_chromo.genes[crossover_point:])),
            np.concatenate((another_chromo.genes[:crossover_point], self.genes[crossover_point:]))
        ]

        generate_child = lambda value: Chromosome(self.num_of_genes, value)
        return list(map(generate_child, children))

    def mutate(self) -> Chromosome:
        selected_bit = randint(0, self.num_of_genes - 1)
        self.genes[selected_bit] = (self.genes[selected_bit] + 1) % 2

        return self

    def set_genes(self, genes_as_int: int):
        abs_value_as_bin = bin(abs(genes_as_int))[2:].rjust(4, '0')
        signed = '1' if genes_as_int < 0 else '0'
        value_as_bin = signed + abs_value_as_bin

        self.genes = np.array(list(value_as_bin), dtype=int)

    def random(num_of_genes:int) -> Chromosome:
        genes = np.random.randint(0, 2, num_of_genes) 
        return Chromosome(num_of_genes, genes)