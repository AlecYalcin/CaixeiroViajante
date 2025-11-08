import sys
import time
from core import *
from algorithms import *
from typing import Callable

USAGE = """
    Usage:
        python3 benchmarks.py <algorithm> <benchmark-file> <result-type>
            <algorithm>         -> 0: permutation, 1: nearest_neighbor, 2: n_nearest_neighbor, 3: group_intersection, 4: n_group_intersection
            <benchmark-file>    -> file location in .txt format with n lines for testing. See 'core/maps/benchmark-n-4.txt' for example
            <result-type>       -> d: mean_distance, t: mean_time
    Exit:
        <mean-distance> -> avarage distance from every testing with the choosen algorithm
        <mean-time>     -> avarage time from every testing with the choosen algorithm
"""

def select_algorithm(code: int) -> Callable:
    """ Função de seleção do algoritmo """

    match code:
        case 0:
            return traveler_permutations
        case 1:
            return nearest_neighbor_heuristic
        case 2:
            return n_nearest_neighbor_heuristic
        case 3:
            return group_intersection_heuristic
        case 4:
            return n_group_intersection_heuristic
        case _:
            print(USAGE)
            raise Exception("The selected algorithm isn't valid.")

if __name__ == "__main__":
    if 3 < len(sys.argv) < 4: 
        print(USAGE)
    else:
        # Argumentos da função
        code = eval(sys.argv[1])
        file = sys.argv[2]
        result_type = sys.argv[3] if len(sys.argv) == 4 else None

        # Selecionando valores
        algorithm = select_algorithm(code)
        maps = Grid.import_maps(file)

        # Calculando a distância média
        mean_distance = 0
        mean_time = 0
        for grid in maps:
            start = time.time()
            result = total_distance(algorithm(grid.points))
            end = time.time()

            mean_distance += result            
            mean_time += (end - start)
        mean_distance /= len(maps)
        mean_time /= len(maps)

        match result_type:
            case "d":
                print(mean_distance)
            case "t":
                print(mean_time)
            case _:
                print(mean_distance, mean_time)


