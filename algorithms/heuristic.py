import random
import sys
from core import *

def nearest_neighbor_heuristic(points: list[Point], initial_index: int | None = None) -> list[Point]:
    """
    Heurística que escolhe um ponto aleatório (ou determinado) e percorre todos os outros pontos considerando
    o próximo ponto a percorrer aquele com a menor distância euclidiana com o atual.
    """

    # Seleciona um ponto aleatório
    choosen_idx = initial_index or random.randint(0, len(points)-1)
    first_point = points.pop(choosen_idx)
    solution = [first_point]

    # Percorre pontos até não sobrar mais nenhum
    current_point = first_point
    while points:
        d_lowest, p_lowest = None, None
        for p in points:
            d_current = euclidean_distance(current_point, p)
            if not d_lowest or d_current < d_lowest:
                d_lowest, p_lowest = d_current, p

        # Uma vez achado o ponto mais curto, adicione na solução
        current_point = p_lowest
        points.remove(p_lowest)
        solution.append(p_lowest)
    
    # Adicionando primeiro ponto e devolvendo resultado
    solution.append(first_point)
    return solution
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "./grid.py <n> or <archive>\n"
            "<n> - quantidade de pontos na grid "
            "<archive> - arquivo de importação"
        )
    else:
        parameter = eval(sys.argv[1])
        match parameter:
            case int():     
                grid = Grid.generate(int(sys.argv[1]))
            case str():
                grid = Grid.import_maps(parameter)[0]
        best = nearest_neighbor_heuristic(grid.points)
        print(total_distance(best))