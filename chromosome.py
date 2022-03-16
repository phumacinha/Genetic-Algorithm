from __future__ import annotations
from calendar import c
from random import randint, random
from typing import List

class Chromosome(object):
    def __init__(self, num_of_genes: int, value: int):
        self.num_of_genes = num_of_genes
        self.value = value
        self.is_alive = True

    def __repr__(self):
        return self.as_bin()

    def as_bin(self, signed:bool = True):
        chromosome_as_bin = bin(self.value)

        is_negative = self.value < 0
        bin_as_str = chromosome_as_bin[3:] if is_negative else chromosome_as_bin[2:]

        sign = '-' if signed and is_negative else ''

        return sign + bin_as_str.rjust(self.num_of_genes, '0')

    def as_unsigned_bin(self):
        return self.as_bin(signed = False)

    def crossover(one_chromo:Chromosome, another_chromo:Chromosome) -> List[Chromosome]:
        crossover_point = randint(0, one_chromo.num_of_genes - 1)
        print('crossover_point', crossover_point)

        children = [
            one_chromo.as_unsigned_bin()[:crossover_point] + another_chromo.as_unsigned_bin()[crossover_point:],
            another_chromo.as_unsigned_bin()[:crossover_point] + one_chromo.as_unsigned_bin()[crossover_point:]
        ]

        both_parents_are_negative = one_chromo.value < 0 and another_chromo.value < 0
        some_parent_is_negative = one_chromo.value < 0 or another_chromo.value < 0

        for i in range(2):
            should_be_negative = both_parents_are_negative

            if not both_parents_are_negative and some_parent_is_negative:
                should_be_negative = random() < 0.5
            
            if should_be_negative:
                children[i] = '-' + children[i]

        generate_child = lambda chromosome_as_bin: Chromosome(one_chromo.num_of_genes, int(chromosome_as_bin, base=2))
        return list(map(generate_child, children))

    def mutate(self) -> Chromosome:
        must_change_sign = random() < .5

        if must_change_sign:
            print('mutação de sinal')
            return Chromosome(self.num_of_genes, self.value * -1)
        else:
            selected_bit = randint(0, self.num_of_genes - 1)
            print('mutação de bit', selected_bit)
            new_chromosome_as_bin = list(self.as_unsigned_bin())
            new_chromosome_as_bin[selected_bit] = 0 if new_chromosome_as_bin[selected_bit] == 1 else 1
            new_chromosome_as_bin = ''.join(map(str, new_chromosome_as_bin))

            factor = -1 if self.value < 0 else 1
            new_chromosome_as_int = int(new_chromosome_as_bin, base = 2) * factor

            return Chromosome(self.num_of_genes, new_chromosome_as_int)

    def random(num_of_genes:int, low:float = -10, high:float = 10) -> Chromosome:
        return Chromosome(num_of_genes, randint(low, high))

    def kill(self):
        self.is_alive = False

chromo1 = Chromosome.random(num_of_genes = 4)
chromo2 = Chromosome.random(num_of_genes = 4)

filho1, filho2 = Chromosome.crossover(chromo1, chromo2)
print('chromo1', chromo1)
print('chromo2', chromo2)
print('filhos', filho1, filho2)
print('filhos depois da mutação', filho1.mutate(), filho2.mutate())

