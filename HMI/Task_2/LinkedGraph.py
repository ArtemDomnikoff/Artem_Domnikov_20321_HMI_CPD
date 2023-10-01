import heapq


class LinkedGraph:
    def __init__(self) -> None:
        self._links = []
        self._vertex = []

    # Добавление в граф новой вершины
    def add_vertex(self, v) -> None:
        if v not in self._vertex:
            self._vertex.append(v)

    # Добавление нового ребра
    def add_link(self, link) -> None:
        for edge in self._links:
            if (link.v1 == edge.v2 and link.v2 == edge.v1) or (link.v1 == edge.v1 and link.v2 == edge.v2):
                break
        else:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    # Нахождение кратчайщего пути между вершинами
    def find_path(self, start_v, stop_v) -> tuple:
        distances = {}  # Словарь для хранения расстояний от начальной вершины до всех остальных вершин
        previous_vertices = {}  # Словарь для хранения предыдущих вершин образующих кратчайший путь
        queue = []  # Очередь для выбора вершины с минимальным расстоянием

        # Инициализация расстояний
        for vertex in self._vertex:
            distances[vertex] = float('inf')
        distances[start_v] = 0

        # Добавление начальной вершины в очередь
        queue.append((distances[start_v], start_v))
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            # Обновление расстояний
            for link in current_vertex.links:
                neighbor_vertex = link.v2 if current_vertex == link.v1 else link.v1
                distance = current_distance + link.dist
                if distance < distances[neighbor_vertex]:
                    distances[neighbor_vertex] = distance
                    previous_vertices[neighbor_vertex] = current_vertex
                    queue.append((distance, neighbor_vertex))

        # Формирование пути
        path = []
        current_vertex = stop_v
        while current_vertex != start_v:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.append(start_v)
        path.reverse()

        # Возвращаем кратчайший путь и список ребер на этом пути
        edges = []
        for i in range(len(path) - 1):
            v1 = path[i]
            v2 = path[i + 1]
            for link in self._links:
                if (link.v1 == v1 and link.v2 == v2) or (link.v1 == v2 and link.v2 == v1):
                    edges.append(link)
                    break

        return path, edges


class Link:
    def __init__(self, v1, v2, dist=1) -> None:
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    # Возвращает атрибут v1
    @property
    def v1(self):
        return self._v1

    # Возвращает атрибут v2
    @property
    def v2(self):
        return self._v2

    # Возвращает атрибут dist
    @property
    def dist(self):
        return self._dist


class Vertex:
    def __init__(self):
        self._links = []

    # Возвращает атрибут links
    @property
    def links(self):
        return self._links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def __str__(self):
        return f'{self._name}'

    def __repr__(self):
        return f'{self._name}'


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)

    def __str__(self):
        return f'{self.v1}, {self.v2}'


if __name__ == '__main__':
    map2 = LinkedGraph()
    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()
    map2.add_link(Link(v1, v2))
    map2.add_link(Link(v2, v3))
    map2.add_link(Link(v2, v4))
    map2.add_link(Link(v3, v4))
    map2.add_link(Link(v4, v5))
    assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
    assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
    map2.add_link(Link(v2, v1))
    assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"
    path = map2.find_path(v1, v5)
    s = sum([x.dist for x in path[1]])
    assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"
    assert issubclass(Station, Vertex) and issubclass(LinkMetro,
                                                      Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"
    map2 = LinkedGraph()
    v1 = Station("1")
    v2 = Station("2")
    v3 = Station("3")
    v4 = Station("4")
    v5 = Station("5")
    map2.add_link(LinkMetro(v1, v2, 1))
    map2.add_link(LinkMetro(v2, v3, 2))
    map2.add_link(LinkMetro(v2, v4, 7))
    map2.add_link(LinkMetro(v3, v4, 3))
    map2.add_link(LinkMetro(v4, v5, 1))
    assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
    assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
    path = map2.find_path(v1, v5)
    assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
    s = sum([x.dist for x in path[1]])
    assert s == 7, "неверная суммарная длина маршрута для карты метро"
