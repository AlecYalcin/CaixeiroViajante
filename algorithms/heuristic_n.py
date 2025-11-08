import sys
from core import (
    Grid, 
    Point,
    total_distance
)
from .heuristic import nearest_neighbor_heuristic

def n_nearest_neighbor_heuristic(points: list[Point]) -> list[Point]:
    """
    Configuração da Heurística de "Vizinho mais Próximo" para selecionar o melhor resultado 
    após testar em todos os pontos iniciais possíveis
    """

    # Calculando a distância de todas as soluções
    best = nearest_neighbor_heuristic(points.copy(), initial_index=0)
    best_distance = total_distance(best)
    for i in range(1, len(points)):
        solution = nearest_neighbor_heuristic(points.copy(), initial_index=i)
        distance = total_distance(solution)
        if distance < best_distance:
            best, best_distance = solution, distance
    return best

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
        best = n_nearest_neighbor_heuristic(grid.points)
        print(total_distance(best))