from copy import deepcopy
from random import randint, random
from chromosome import Chromosome
from typing import List

class GeneticAlgorithm(object):
    def __init__(self, mating_pool_size:int, mutation_rate:float, crossover_rate:float, number_of_generations:int, min_value:int, max_value:int):
        self.mating_pool_size = mating_pool_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.number_of_generations = number_of_generations
        self.min_value = min_value
        self.max_value = max_value

    def generate_initial_population(self, population_size:int = 4) -> List[Chromosome]:
        population = list()

        while len(population) < population_size:
            chromo = Chromosome.random(num_of_genes = 5)
            self.adjust_chromosome_genes(chromo)
            population.append(chromo)

        return population

    def objective_function(self, value:int) -> int:
        return value*value - 3*value + 4

    def calculate_population_fitness(self, population:List[Chromosome]) -> List[int]:
        fitness:List[int] = []
        for chromosome in population:
            fitness_value = self.objective_function(chromosome.as_int())
            fitness.append(fitness_value)

        return fitness

    def tournament(self, population:List[Chromosome]) -> List[Chromosome]:
        fitness:List[int] = self.calculate_population_fitness(population)

        print('Fitness', fitness)

        population_aux = deepcopy(population)
        if len(population) <= self.mating_pool_size:  # Caso da população inicial
            return population_aux
        
        parents = []
        while len(parents) < self.mating_pool_size:
            index_one = randint(0, len(population_aux) - 1)
            chromosome_one = population_aux.pop(index_one)

            index_two = randint(0, len(population_aux) - 1)
            chromosome_two = population_aux.pop(index_two)

            if (fitness[index_one] > fitness[index_two]):
                parents.append(chromosome_one)
            else:
                parents.append(chromosome_two)

        return parents

    def get_best_result(self, population:List[Chromosome]) -> Chromosome:
        population_fitness = self.calculate_population_fitness(population)
        index = population_fitness.index(max(population_fitness))
        return population[index]

    def adjust_chromosome_genes(self, chromosome:Chromosome):
        if chromosome.as_int() > self.max_value:
            chromosome.set_genes(self.max_value)
        
        if chromosome.as_int() < self.min_value:
            chromosome.set_genes(self.min_value)

    def main(self):
        population:List[Chromosome] = self.generate_initial_population()

        for generation in range(self.number_of_generations):
            print('\n\n' + '-'*20 + f'\nGeneration #{generation}\n')

            # printar populacao
            print('Population', population)

            parents = self.tournament(population)

            # printar parents
            print('Parents', parents)

            parents_aux = deepcopy(parents)
            offspring:List[Chromosome] = []
            while len(parents_aux) > 0:
                index_one = randint(0, len(parents_aux) - 1)
                parent_one = parents_aux.pop(index_one)

                index_two = randint(0, len(parents_aux) - 1)
                parent_two = parents_aux.pop(index_two)

                should_crossover = random() < self.crossover_rate

                if should_crossover:
                    children = parent_one.crossover(parent_two)

                    for child in children:
                        self.adjust_chromosome_genes(child)

                    offspring = [*offspring, *children]
                else:
                    offspring.append(parent_one)
                    offspring.append(parent_two)

            # printar offspring apos crossover
            print('Offspring', offspring)

            for child in offspring:
                should_mutate = random() < self.mutation_rate

                if should_mutate:
                    child.mutate()
                    self.adjust_chromosome_genes(child)
            
            # printar offspring apos mutacao
            print('Offspring after mutation', offspring)

            population = [*parents, *offspring]

        print('\n' + '-'*20 + f'\nLAST POPULATION: {population}')
        print(f'BEST RESULT {self.get_best_result(population)}')

if __name__ == '__main__':
    genetic_algorithm = GeneticAlgorithm(mating_pool_size = 4, mutation_rate = .01, crossover_rate = .7, number_of_generations = 5, min_value = -10, max_value = 10)
    genetic_algorithm.main()