import sys
import random
from core import *

class Group:
    elements: list[Point]
    centroid: Point

    def __init__(self, elements=..., centroid=...):
        if elements == ...:
            elements = []
        self.elements = elements
        if centroid == ...:
            centroid = Point(0, 0, "PC")
        self.centroid = centroid

    def _calculate_centroid(self) -> None:
        x_mean = 0
        y_mean = 0
        for e in self.elements:
            x_mean += e.longitude
            y_mean += e.latitude
        x_mean /= len(self.elements)
        y_mean /= len(self.elements)
        self.centroid = Point(longitude=x_mean, latitude=y_mean, name=self.centroid.name)

    def is_empty(self) -> bool:
        if len(self.elements) > 0:
            return False
        return True

    @staticmethod
    def sum_of_distances(points: list["Point"]) -> float:
        d = 0
        for p in range(0, len(points)-1):
            print(f"{points[p]} ->", end=" ")
            d += euclidean_distance(points[p], points[p+1])
        print(f"{points[len(points)-1]}\n")
        return d

    def __str__(self) -> str:
        return f"Centróide: {self.centroid}, Elementos: {[str(e) for e in self.elements]}"

def _select_the_best_starter(points: list[Point]) -> int:
    """
    Função que seleciona o candidato mais longe por ser o melhor para a heurística
    """

    # Se considera que todos os pontos fazem parte do mesmo grupo
    grupo = Group(
        elements=points
    )
    grupo._calculate_centroid()

    # Agora pesquiso qual o elemento mais longe 
    d_highest = 0
    p_highest = None
    for i in range(len(points)):
        d = euclidean_distance(grupo.centroid, points[i])
        if d > d_highest:
            d_highest = d
            p_highest = i

    # Retorna o indice
    return p_highest


def analyze_current_point(current_point: Point, groups: list[Group], threshold: float = 1.0):
    """ 
    Análise do ponto atual seguindo os padrões da heurística. Compara o grupo atual com todos os pontos de todos os grupos.
    Se os pontos dos outros grupos estiverem mais próximos do ponto atual do que seus respectivos grupos, então os aloca
    em um novo grupo.
    """

    # Calcular os centróides dos grupos
    for i in range(len(groups)):
        groups[i]._calculate_centroid()

    # Comparar a distância dos centróides e o grupo atual
    recently_groups = []
    for g in groups:
        new_group = Group(centroid=Point(0, 0, f"C{random.randint(0, 999)}"))
        current_distance_from_centroid = euclidean_distance(current_point, g.centroid)
        for e in g.elements:
            current_distance_from_element = euclidean_distance(current_point, e)
            if current_distance_from_element < (current_distance_from_centroid * threshold):
                new_group.elements.append(e)
                g.elements.remove(e)
        if not new_group.is_empty():
            recently_groups.append(new_group) 
    groups.extend(recently_groups)

    # Selecione o grupo com o centróide mais pŕoximo
    closest_group, closest_distance = None, None
    for i in range(len(groups)):
        groups[i]._calculate_centroid()
        distance = euclidean_distance(current_point, groups[i].centroid)
        if closest_distance == None or distance < closest_distance:
            closest_group, closest_distance = i, distance
   
    # Pegue o primeiro elemento do grupo e retire ele do grupo
    return groups[closest_group].elements.pop(0)

def group_intersection_heuristic(points: list[Point], threshold: float = 1.0, initial_index: int | None = None) -> list[Point]:
    """
    Heurística que realiza a seleção dos melhores caminhos através da seleção de grupos mais próximos identificados.\n
    Utiliza de comparação do ponto atual com outros grupos para verificar se existem elementos dentro de um grupo que estão
    mais próximos do elemento do que do centróide calculado. 
    """

    # Selecionando o primeiro ponto
    first_point = points.pop(initial_index or _select_the_best_starter(points))
    solution = [first_point]

    # Alocando o restante dos pontos para o primeiro grupo geral
    first_group = Group(
        elements=points,
        centroid=Point(0, 0, f"C{random.randint(0, 999)}")
    )

    # Iterando sobre os grupos até não sobrar mais nenhum ou não existirem mais ponto
    groups = [first_group]
    next_point = first_point
    while groups:
        next_point = analyze_current_point(next_point, groups, threshold)
        solution.append(next_point)

        # Removendo os grupos
        groups_to_remove = []
        for i in range(len(groups)):
            if groups[i].is_empty():
                groups_to_remove.append(i)
        for i in groups_to_remove:
            groups.pop(i)

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
        best = group_intersection_heuristic(grid.points)
        print(total_distance(best))