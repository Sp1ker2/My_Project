import random
import numpy as np

from deap import base
from deap import creator
from deap import tools

LOW, UP = -3, 3
eta = 20
length_chrom = 2

population_size = 200
p_crossover = 0.9
p_mutation = 0.2
max_generation = 50

def eval_func(individual):
    x, y = individual
    return 1 / (1 + x ** 2 + y ** 2),
population_size

def random_point(a, b):
    return [random.uniform(a, b), random.uniform(a, b)]


def create_toolbox():
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox

    toolbox.register("randomPoint",random_point, LOW, UP)
    toolbox.register("individualCreator" ,tools.initIterate, creator.Induvidual, toolbox.randompoint)
    toolbox.register("populationCreator",tools.initIterate, list, toolbox.induvidualCreator)

    toolbox.register('evalute', eval_func)
    toolbox.register('select', tools.selTournament, tournsize=23)
    toolbox.register('mate', tools.cxSimulatedBinaryBounded, low=LOW, up=UP, eta=eta)
    toolbox.register('mate', tools.mutPolynomialBounded(), low=LOW, up=UP, eta=eta,indpb= 1.0/length_chrom)
    stats = tools.Statistics(lambda ind:ind.fitness.values)
    stats.register('min',np.min)
    stats.register('avg',np.mean)
    return toolbox


if __name__ == "__main__":
    toolbox=create_toolbox()
    random.seed(7)
    population = toolbox.populationCreator(n=500)
    num_generation = 100
    print('\nstatics')
    fitnsses = list(map(toolbox.evalute,population))
    for ind,fit in zip(population,fitnsses):
        ind.fitness.values=fit
    print('\nevalution ',len(population))
    for g in range(num_generation):
        print('\n ======generation ',g)
    offspring = toolbox.select(population, len(population))

    offspring = list(map(toolbox.clone, offspring))
    # Apply crossover and mutation on the offspring
    for child1, child2 in zip(offspring[::2],offspring[1::2]):
        # Cross two individuals
        if random.random() < p_crossover:
            toolbox.mate(child1, child2)

    # "Forget" the fitness values of the children
            del child1.fitness.values
            del child2.fitness.values
    for mutant in offspring:
        if random.random()<p_mutation:
            toolbox.mutate(mutant)
            del mutant.fitness.values
    invalid_ind = [ind for ind in offspring if not ind.fitness.values]
    fitnsses = map(toolbox.evalute,invalid_ind)
    for ind,fit in zip(invalid_ind,fitnsses):
        ind.fitness.values = fit
    print('evaluted ', len(invalid_ind))
    population[:]=offspring
    fits = [ind.fitness.values[0] for ind in population]

    length= len(population)
    mean =  sum(fits)/length
    sum2 = sum(x*x for x in fits)
    std  = abs(sum2/length-mean**2)**0.5
    print('min = ',min(fits),'max = ',max(fits))
    print('Average = ',round(mean,2),'standart = ',round(std,2))
    print('\n======evolution')
    best_ind = tools.selBest(population,1)[0]
    print('\n== best induvidual',best_ind)
    print('\nnumber of ones',sum(best_ind))

