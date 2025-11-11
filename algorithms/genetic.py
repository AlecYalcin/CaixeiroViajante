import random
import sys
from core import *

EPOCHS = 100
MAX_PARENTS = int(EPOCHS * 0.20)
MAX_CHILDREN = int(MAX_PARENTS * (MAX_PARENTS-1))
MUTATION_CHANCE = 0.25

def mutate(child: list[Point]) -> list[Point]:
    """
    Realiza uma mutação em um campo aleatório da lista de pontos
    """

    first_index = random.randint(0, len(child)-1)
    second_index = random.randint(0, len(child)-1)
    while second_index == first_index:
        second_index = random.randint(0, len(child)-1)
    child[first_index], child[second_index] = child[second_index], child[first_index]
    return child

def mate(first: list[Point], second: list[Point]) -> list[Point]:
    """
    Cruza dois pontos para gerar um novo ponto de modo cícloco
    """

    # Criando o filho base
    size = len(first)
    child = [None]*size

    # Percorrendo o primeiro pai até completar o ciclo de repetição
    position = 0
    while first[position] not in child:
        child[position] = first[position]
        position = second.index(first[position])
    
    # Alocando o restante dos pontos a partir do segundo pai
    child = [child[i] if child[i] is not None else second[i] for i in range(len(second))]

    # Aplicando mutação genética
    if random.random() <= MUTATION_CHANCE:
        child = mutate(child)

    return child


def mating_season(parents: list[list[Point]], kids_len: int = MAX_CHILDREN) -> list[list[Point]]:
    """
    Cruza todos os pontos enviados de forma a criar filhos com características misturadas
    entre todos eles.
    """

    # Cruza toda a população restante
    children = []
    for i, p1 in enumerate(parents):
        for j, p2 in enumerate(parents):
            if i != j:
                child = mate(p1, p2)
                children.append(child)
            if len(children) >= kids_len:
                return children[:kids_len]
    return children

def genetic_heuristic(points: list[Point]) -> list[Point]:
    """
    Meta-heurística para o problema do caixeiro viajante com algoritmo genético.
    """

    # Gerar uma População aleatória inicial
    population = [random.sample(points, len(points)) for _ in range(100)]

    # Ordenar população pela menor distância total
    population = sorted(population, key=lambda k: total_distance(k))

    # Delimitar a quantidade de parentes para a próxima geração
    epochs = EPOCHS
    max_parents = MAX_PARENTS
    while epochs:
        parents = population[:max_parents]
        children = mating_season(parents)
        population = parents + children
        population = sorted(population, key=lambda k: total_distance(k))
        epochs = epochs - 1
    return population[0]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "./grid.py <n> or <archive>\n"
            "<n> - quantidade de pontos na grid "
            "<archive> - arquivo de importação"
        )
    else:
        try:
            parameter = eval(sys.argv[1])
        except Exception:
            parameter = sys.argv[1]
        match parameter:
            case int():     
                grid = Grid.generate(int(sys.argv[1]))
            case str():
                grid = Grid.import_maps(parameter)[0]
        best = genetic_heuristic(grid.points)
        print(total_distance(best))