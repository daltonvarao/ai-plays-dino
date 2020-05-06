import numpy as np
import random
import time
from datetime import datetime

from lib.neural_network import F2AN2

"""
    Genetic Algorithm

    1# Initialize population

    While i <= population_size
        2# Avaliate individuals
        3# Mate individuals pairs for recombination
        4# Recombinate
        6# Renew population
        5# Apply Mutation in individuals of new population
"""

class Individual:

    def __init__(self, net_layers, genes=None):
        self.brain = F2AN2(*net_layers)

        if np.any(genes):
            self.genes = genes

        self.genes = self.brain.linearize_weights()
        self.score = 0
        self.build_brain()
        self.outputs = []

    def save_score(self, score):
        print("Score:", score)
        self.score = score

    def activate(self, x):
        output = self.brain.predict(x)
        self.outputs.append(output)
        return output

    def build_brain(self):
        self.brain.load_weights(self.genes)

    def has_experience(self):
        return len(self.outputs) >= 1

    def __repr__(self):
        return "<Individual score: {} >".format(self.score)


class Generation:

    def __init__(self, pop_size, net_layers):
        self.pop_size = pop_size
        self.net_layers = net_layers
        self.current_individual_index = 0
        self.over = False

    def initialize(self, population=None):
        if population:
            self.population = population
        else:
            self.population = [Individual(self.net_layers) for _ in range(self.pop_size)]

    def avaliate(self):
        return sorted(self.population, key=lambda individual: individual.score, reverse=True)

    @property
    def current_individual(self):
        return self.population[self.current_individual_index]

    def next_individual(self):
        print("Individual - {}/{}".format(self.current_individual_index + 1, self.pop_size))
        if self.current_individual_index >= (self.pop_size - 1):
            self.over = True
            return False

        if not self.over:
            self.current_individual_index += 1

    def ended(self):
        return self.current_individual_index >= (self.pop_size - 1)


class GeneticAlgorithm:

    def __init__(self, pop_size=16, net_layers=(3, 4, 4, 1), cr=0.6, mr=0.01, train_mode=True, bests_num=4):
        self.train_mode = train_mode
        self.pop_size = pop_size
        self.net_layers = net_layers
        self.cr = cr
        self.mr = mr
        self.gnumber = 1
        self.new_generation()
        self.bests_num = bests_num

    def save_many(self, filename=None):
        genes = []

        if not filename:
            filename = "ga-{}.npy".format(datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))
        
        for ind in self.generation.population:
            genes.append(ind.genes)
        np.save(filename, np.array(genes))

    def load_many(self, filename):
        genes_list = np.load(filename)

        for genes, ind in zip(genes_list, self.generation.population):
            ind.genes = genes
            ind.build_brain()

    def select_by_tournament(self, population):
        selected1 = random.choice(population)
        selected2 = random.choice(population)

        if selected1.score >= selected2.score:
            return selected1
        return selected2

    def select_parents(self, population):
        return [
            self.select_by_tournament(population),
            self.select_by_tournament(population)
        ]

    def build_new_population(self, population):
        new_population = population[:self.bests_num].copy()

        while len(new_population) < self.pop_size:
            parents = self.select_parents(population)
            new_population.extend(self.apply_mutation(self.crossover(parents)))
        
        return new_population


    def crossover(self, parents):
        point = random.randint(1, len(parents[0].genes) - 2)

        if random.random() <= self.cr:
            parent1 = Individual(self.net_layers, np.concatenate((parents[0].genes[:point], parents[1].genes[point:])))
            parent2 = Individual(self.net_layers, np.concatenate((parents[1].genes[:point], parents[0].genes[point:])))

            return [parent1, parent2]

        return parents

    def apply_mutation(self, population):
        for individual in population:
            self.mutation(individual)

        return population

    def mutation(self, individual):
        for i in range(len(individual.genes)):
            if random.random() <= self.mr:
                individual.genes[i] += individual.genes[i] * (random.random() - .5) * 3 + (random.random() - 0.5)

    def avaliate(self):
        population = self.generation.avaliate()
        new_population = self.build_new_population(population)
        return new_population

    def new_generation(self, population=None):
        print('New Generation invoked - {}'.format(self.gnumber))
        self.gnumber += 1
        self.generation = Generation(self.pop_size, self.net_layers)
        self.generation.initialize(population)
