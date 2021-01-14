from unittest import TestCase
from Ex3.DiGraph import DiGraph


class TestDiGraph(TestCase):
    def setUp(self) -> None:
        self._graph = DiGraph()
        self._graph.add_node(node_id=1, pos=(1.6, 2, 3))
        self._graph.add_node(node_id=2, pos=(2, 3, 4))
        self._graph.add_node(node_id=3, pos=(3, 4, 5))
        self._graph.add_edge(1, 2, 5)
        self._graph.add_edge(2, 3, 6)
        self._graph.add_edge(3, 1, 8)

    def test_v_size(self):
        self.assertEqual(3, self._graph.v_size())

    def test_e_size(self):
        self.assertEqual(3, self._graph.e_size())

    def test_get_all_v(self):
        g = self._graph.get_all_v()
        self.assertEqual(self._graph.get_node(1), g.get(1))

    def test_all_in_edges_of_node(self):
        e = self._graph.all_in_edges_of_node(1)
        self.assertEqual(e.get(3), self._graph.all_in_edges_of_node(1).get(3))

    def test_all_out_edges_of_node(self):
        e = self._graph.all_out_edges_of_node(2)
        self.assertEqual(e.get(3), self._graph.all_out_edges_of_node(2).get(3))

    def test_get_mc(self):
        self._graph.remove_node(2)
        self.assertEqual(7, self._graph.get_mc())

    def test_add_edge(self):
        g = self._graph
        g.add_edge(1, 3, 6)
        self.assertEqual(4, g.e_size())

    def test_add_node(self):
        g = self._graph
        g.add_node(4, (4, 5, 6))
        self.assertEqual(4, g.v_size())

    def test_remove_node(self):
        g = self._graph
        g.remove_node(2)
        self.assertEqual(2, g.v_size())
        self.assertEqual(1, g.e_size())

    def test_remove_edge(self):
        g = self._graph
        g.remove_edge(1, 2)
        self.assertEqual(2, g.e_size())

    def test_get_node(self):
        v = self._graph.get_node(1)
        self.assertEqual(v.get_location(), self._graph.get_node(1).get_location())


