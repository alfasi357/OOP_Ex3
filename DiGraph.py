from Ex3.GraphInterface import GraphInterface
from Ex3.Node_Data import Node_Data as n

"""
This class represents directed weighted graph and it's implementations.
contains:
esize
mc
graph
alledgeinsdie
alledgeoutside
"""


class DiGraph(GraphInterface):
    def __init__(self):
        self._esize = 0
        self._mc = 0
        self._graph = {}
        self._alledgeinside = {}
        self._alledgeoutside = {}

    def v_size(self) -> int:
        """
        this method return the amount of nodes  in the graph
        :return:  v_size
        """
        return len(self._graph)

    def e_size(self) -> int:
        """
        this method return the number of edges in the graph
        :return: e_size
        """
        return self._esize

    def get_all_v(self) -> dict:
        """
        this method return dictionary of all the nodes in the graph
        :return: get_all_v
        """
        if self._graph is None:
            return {}
        return self._graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        this method return dictionary of the edges that enter to the node
        :param id1:
        :return: all_in_edges_of_node
        """
        return self._alledgeinside.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        this method return dictionary of the edges that coming out of the chosen node
        :param id1:
        :return: all_edges_of_node
        """
        return self._alledgeoutside.get(id1)

    def get_mc(self) -> int:
        """
        this method return the amount of actions that been made on the graph
        :return: get_mc
        """
        return self._mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        this method add an edge to the graph
        :param id1:
        :param id2:
        :param weight:
        :return:
        """
        if self._graph.get(id1) is not None and self._graph.get(id2) is not None and weight > 0:
            if self._alledgeoutside[id1].get(id2) is None:
                self._alledgeoutside[id1][id2] = weight
                self._alledgeinside[id2][id1] = weight
                self._mc += 1
                self._esize += 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        this method add node to the graph
        :param node_id:
        :param pos:
        :return:
        """
        if self.get_node(node_id) is None:
            temp = n(key=node_id, geo=pos)
            self._graph[node_id] = temp
            self._alledgeinside[node_id] = {}
            self._alledgeoutside[node_id] = {}
            self._mc += 1
            return True

        return False

    def remove_node(self, node_id: int) -> bool:
        """
        this method remove a chosen node from the graph
        :param node_id:
        :return:
        """
        if self._graph is None:
            return False
        if self._graph[node_id] is not None:
            for key in self._graph:
                if self._alledgeinside[key].get(node_id) is not None:
                    self._alledgeinside[key].pop(node_id)
                if self._alledgeoutside[key].get(node_id) is not None:
                    self._alledgeoutside[key].pop(node_id)
            c = len(self._alledgeinside[node_id])
            b = len(self._alledgeoutside[node_id])
            self._alledgeinside.pop(node_id)
            self._alledgeoutside.pop(node_id)
            self._graph.pop(node_id)
            self._mc += 1
            self._esize -= (b + c)
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        this method remove a chosen edge from the graph
        :param node_id1:
        :param node_id2:
        :return:
        """
        if self._alledgeinside[node_id2].get(node_id1) is not None:
            self._alledgeinside[node_id2].pop(node_id1)
            self._alledgeoutside[node_id1].pop(node_id2)
            self._mc += 1
            self._esize -= 1
            return True
        return False

    def get_node(self, key) -> n:
        """
        this method return a node of chosen key
        :param key:
        :return:
        """
        return self._graph.get(key)
