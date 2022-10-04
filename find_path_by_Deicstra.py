class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, d):
        self._dist = d


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if len(list(filter(lambda x: (x.v1 == link.v1 or x.v1 == link.v2) and (x.v2 == link.v2 or x.v2 == link.v1),
                           self._links))) < 1:
            self._links.append(link)
            self.add_vertex(link.v1)
            link.v1.links.append(link)
            self.add_vertex(link.v2)
            link.v2.links.append(link)

    @staticmethod
    def find_lowest_cost_node(costs, processed):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost_node = node
                lowest_cost = cost
        return lowest_cost_node

    @staticmethod
    def personal_linked_nodes(v):
        """возвращает список вершин, с которыми связана v"""
        box = []
        for i in v.links:
            box.append(i.v1 if i.v1 != v else i.v2)
        return box

    def creating_dicts(self, start):
        graph = {}
        costs = {}
        parents = {}

        graph[start] = {}
        for i in self.personal_linked_nodes(start):
            graph[start][i] = next(
                filter(lambda x: x.v1 == start and x.v2 == i or x.v2 == start and x.v1 == i, start.links)).dist
        for j in self._vertex:
            if j != start:
                graph[j] = {}
                for q in self.personal_linked_nodes(j):
                    graph[j][q] = next(
                        filter(lambda x: x.v1 == j and x.v2 == q or x.v2 == j and x.v1 == q, j.links)).dist

        for i in self._vertex:
            if i != start:
                if i not in self.personal_linked_nodes(start):
                    costs[i] = float("inf")
                else:
                    costs[i] = graph[start][i]

        for i in self._vertex:
            if i not in self.personal_linked_nodes(start):
                parents[i] = None
            else:
                parents[i] = start

        return graph, costs, parents

    def find_path(self, start_v, stop_v):
        graph, costs, parents = self.creating_dicts(start_v)
        processed = [start_v]
        node = self.find_lowest_cost_node(costs, processed)
        while node is not None:
            cost = costs[node]
            neighbors = graph[node]
            for n in neighbors.keys():
                if n in processed:
                    continue
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = node
            processed.append(node)
            node = self.find_lowest_cost_node(costs, processed)

        path = []
        path_links = []

        x = stop_v
        path.append(x)
        while parents[x] is not None:
            l = parents[x]
            path_links += list(filter(lambda i: i.v1 == x and i.v2 == l or i.v1 == l and i.v2 == x, self._links))
            path.append(l)
            x = l
        path.reverse()

        return path, path_links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self.dist = dist


map2 = LinkedGraph()
v1 = Station("китай город")
v2 = Station("dkusp")
v3 = Station("hina tpwn")
v4 = Station("gag bdvksv pp")
v5 = Station("dlada hh 89")

map2.add_link(LinkMetro(v1, v2, 3453))
map2.add_link(LinkMetro(v2, v3, 23))
map2.add_link(LinkMetro(v1, v5, 2))
map2.add_link(LinkMetro(v5, v4, 12))
map2.add_link(LinkMetro(v3, v4, 232))
print(map2.find_path(v1, v4))
