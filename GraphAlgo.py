import json
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC
from queue import PriorityQueue

from Ex3.GraphInterface import GraphInterface
from Ex3.GraphAlgoInterface import GraphAlgoInterface
from Ex3.DiGraph import DiGraph

"""
This class represent an algorithms on the graph, meaning more complex methods on the graph.
this class contains:
DiGraph   
"""
class GraphAlgo(GraphAlgoInterface, ABC):
    def __init__(self, g: DiGraph = None):
        self._algo = g

    def get_graph(self) -> GraphInterface:
        """
        this method return a graph
        :return:
        """
        return self._algo

    def load_from_json(self, file_name: str) -> bool:
        """
        this method load a json file into a graph and return true if the load success
        :param file_name:
        :return: true or false accordingly
        """
        graph = DiGraph()
        try:
            with open(file_name) as json_file:
                data = json.load(json_file)
                for p in data["Nodes"]:
                    node_id = p.get("id")
                    pos = None
                    if p.get("pos") is not None:
                        pos = p.get("pos")
                        ls = pos.split(",")
                        pos = (float(ls[0]), float(ls[1]), float(ls[2]))
                    graph.add_node(node_id, pos)
                for p2 in data["Edges"]:
                    src = p2.get("src")
                    dest = p2.get("dest")
                    w = p2.get("w")
                    graph.add_edge(src, dest, w)
                self._algo = graph
                return True
        except Exception as e:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        this method save a graph to a json file and return true if the save success, otherwise return false
        :param file_name:
        :return: true or false accordingly
        """
        if self._algo is None:
            return False
        data = {"Nodes": [], "Edges": []}
        nodes = self._algo.get_all_v()
        for key, pos in nodes.items():
            data["Nodes"].append({"pos": str(pos.get_location()[0]) + "," + str(pos.get_location()[1]) + "," + str(
                pos.get_location()[2]), "id": key})
            edges = self._algo.all_out_edges_of_node(key)
            for key2, weight in edges.items():
                data["Edges"].append({"src": key, "dest": key2, "w": weight})
        try:
            with open(file_name, 'w') as outfile:
                json.dump(data, outfile)
                return True
        except Exception as e:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        this method find the shortest path of two chosen nodes and return it as a list and also the sum of weight
        the path includes
        :param id1:
        :param id2:
        :return: shortest_path
        """
        if id1 == id2:
            return 0, [id1]
        if self._algo is None:
            return float('inf'), []
        if self._algo.get_node(id1) is None or self._algo.get_node(id2) is None:
            return float('inf'), []
        for key in self._algo.get_all_v():
            self._algo.get_node(key).set_weight(float('inf'))
        self._algo.get_node(id1).set_weight(0)
        nodes = self._algo.get_all_v()
        lis = PriorityQueue()
        lis.put((nodes[id1].get_weight(), id1))
        if id1 == id2:
            return 0, lis
        while not lis.empty():
            temp = lis.get()[1]
            for key2, weight in self._algo.all_out_edges_of_node(temp).items():
                if self._algo.get_node(key2).get_weight() == float('inf'):
                    self._algo.get_node(key2).set_weight(weight + self._algo.get_node(temp).get_weight())
                    lis.put((nodes.get(key2).get_weight(), key2))
                elif self._algo.get_node(key2).get_weight() > weight + self._algo.get_node(temp).get_weight():
                    self._algo.get_node(key2).set_weight(weight + self._algo.get_node(temp).get_weight())
        if nodes[id2].get_weight() == float('inf'):
            return float('inf'), []
        lis2 = [id2]
        temp2 = id2
        while temp2 != id1:
            for key3, weight2 in self._algo.all_in_edges_of_node(temp2).items():
                if nodes.get(temp2).get_weight() == weight2 + nodes.get(key3).get_weight():
                    lis2.insert(0, key3)
                    temp2 = key3
                    break

        return nodes.get(id2).get_weight(), lis2

    def connected_component(self, id1: int) -> list:
        """
        this method find all the strongly connected nodes to the chosen node and return all of them as a list
        :param id1:
        :return: connected_component(id)
        """
        if self._algo is None or self._algo.get_node(id1) is None:
            return []
        nodes = self._algo.get_all_v()
        for key in nodes:
            nodes.get(key).set_tag(-1)

        nodes.get(id1).set_tag(0)
        lis = [id1]
        lis2 = [id1]
        lis3 = [id1]
        lis4 = [id1]
        lis5 = []
        while len(lis) != 0:
            temp = lis.pop(0)
            edge_out = self._algo.all_out_edges_of_node(temp)
            for key2 in edge_out.keys():
                if nodes.get(key2).get_tag() == -1:
                    lis.append(key2)
                    nodes.get(key2).set_tag(0)

        for key in nodes:
            if nodes.get(key).get_tag() == 0 and key != id1:
                lis3.append(key)
            nodes.get(key).set_tag(-1)

        while len(lis2) != 0:
            temp2 = lis2.pop(0)
            edge_in = self._algo.all_in_edges_of_node(temp2)
            for key3 in edge_in:
                if nodes.get(key3).get_tag() == -1:
                    lis2.append(key3)
                    nodes.get(key3).set_tag(0)

        for key in nodes:
            if nodes.get(key).get_tag() == 0 and key != id1:
                lis4.append(key)
            nodes.get(key).set_tag(-1)

        for t1 in lis3:
            for t2 in lis4:
                if t1 == t2:
                    lis5.append(t1)
                    break

        return lis5

    def connected_components(self) -> list:
        """
        this method use the method above to find to the nodes the strongly connected components and then return it
        as list of lists- each one of the inside lists contain connected_component(id)
        :return: connected_component
        """
        if self._algo is None:
            return []
        lis = []
        lis2 = []
        lis3 = []
        for id_node in self._algo.get_all_v().keys():
            lis.append(id_node)
        while len(lis) != 0:
            key = lis.pop(0)
            lis2 = self.connected_component(key)
            lis3.append(lis2)
            for key2 in lis2:
                if key2 != key:
                    lis.remove(key2)
        return lis3

    def plot_graph(self) -> None:
        """
        this method drawing and creating a graph, not including the z location and work only in the x and y axis,
        creating the vertexes and connected them with the wanted edges
        :return:s
        """
        if self._algo is None:
            return
        nodes = self._algo.get_all_v()
        x_vals = []
        y_vals = []
        h_x = 0
        l_x = float("inf")
        h_y = 0
        l_y = float("inf")
        for key, pos in nodes.items():
            if pos.get_location() is not None:
                x_vals.append(pos.get_location()[0])
                y_vals.append(pos.get_location()[1])
                if pos.get_location()[0] > h_x:
                    h_x = pos.get_location()[0]
                elif pos.get_location()[0] < h_x:
                    l_x = pos.get_location()[0]
                if pos.get_location()[1] > h_y:
                    h_y = pos.get_location()[1]
                elif pos.get_location()[1] < h_y:
                    l_y = pos.get_location()[1]

        if l_x == float('inf'):
            l_x = 0
        if h_x == 0:
            h_x = 10
        if l_y == float('inf'):
            l_y = 0
        if h_y == 0:
            h_y = 10

        for key, pos in nodes.items():
            if pos.get_location() is None:
                t_x = np.random.uniform(low=l_x, high=h_x, size=1)
                x_vals.append(t_x)
                t_y = np.random.uniform(low=l_y, high=h_y, size=1)
                y_vals.append(t_y)
                pos.set_location((t_x, t_y, 0))
        fig, ax = plt.subplots()
        ax.scatter(x_vals, y_vals)
        plt.plot(x_vals, y_vals)
        plt.show()
