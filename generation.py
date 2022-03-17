from __future__ import annotations
import numpy as np
from chromosome import Chromosome

class Generation(object):
    def __init__(self, chromosomes, parents, generation_number: int):
        self.chromosomes = chromosomes
        self.parents = parents
        self.generation_number = generation_number

    def __repr__(self):
        photo = "-"*20 + "\nGeneration: " + str(self.generation_number) + "\n\n"
        photo += "Chromosomes:\n"
        for chromosome in self.chromosomes:
            photo += str(chromosome) + " "
        photo += "\n\nParents:\n"
        for parent in self.parents:
            photo += str(parent) + " "
        photo += "\n" + ("-"*20)
        return photo

chromo1 = Chromosome.random(num_of_genes = 4)
chromo2 = Chromosome.random(num_of_genes = 4)
gen = Generation([chromo1, chromo2], [chromo1, chromo2], 1)
print(gen)