import sys
import time
from core import *
from algorithms import *
from typing import Callable

USAGE = """
    Usage:
        python3 benchmarks.py <algorithm> <benchmark-file> <result-type>
            <algorithm>         -> 0: permutation, 1: nearest_neighbor, 2: n_nearest_neighbor, 3: group_intersection, 4: n_group_intersection. 5: genetic
            <benchmark-file>    -> file location in .txt format with n lines for testing. See 'core/maps/benchmark-n-4.txt' for example
            <result-type>       -> d: mean_distance, t: mean_time
    Exit:
        <mean-distance> -> avarage distance from every testing with the choosen algorithm
        <mean-time>     -> avarage time from every testing with the choosen algorithm
"""

def select_algorithm(code: int) -> Callable:
    """ Função de seleção do algoritmo """

    match code:
        case "permutation":
            return traveler_permutations
        case "heuristic":
            return nearest_neighbor_heuristic
        case "heuristic_n":
            return n_nearest_neighbor_heuristic
        case "my_heuristic":
            return group_intersection_heuristic
        case "my_heuristic_n":
            return n_group_intersection_heuristic
        case "genetic":
            return genetic_heuristic
        case _:
            print(USAGE)
            raise Exception("The selected algorithm isn't valid.")

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4: 
        print(USAGE)
    else:
        # Argumentos da função
        code = sys.argv[1]
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


