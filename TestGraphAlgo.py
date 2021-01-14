from unittest import TestCase
from Ex3.GraphAlgo import GraphAlgo
from Ex3.DiGraph import DiGraph


class TestGraphAlgo(TestCase):
    def setUp(self) -> None:
        self.g = DiGraph()
        self.g.add_node(node_id=1, pos=(1, 2, 3))
        self.g.add_node(node_id=2, pos=(2, 3, 4))
        self.g.add_node(node_id=3, pos=(3, 4, 5))
        self.g.add_edge(1, 2, 5)
        self.g.add_edge(2, 3, 6)
        self.g.add_edge(3, 1, 8)
        self.g2 = GraphAlgo(self.g)

    def test_get_graph(self):
        d = self.g2.get_graph()
        self.assertEqual(self.g2.get_graph().e_size(), d.e_size())

    def test_save_and_load_from_json(self):
        self.g2.save_to_json("file_test")
        f = self.g2.load_from_json("file_test")
        self.assertTrue(f)

    def test_shortest_path(self):
        b = self.g2.shortest_path(1, 3)
        self.assertEqual(b[0], 11)

    def test_connected_component(self):
        self.g.add_node(4)
        self.g.add_node(5)
        self.g.add_edge(4, 5, 6)
        self.g.add_edge(5, 4, 3)
        b = self.g2.connected_component(1)
        c = self.g2.connected_component(4)
        self.assertEqual(len(b), len(c) + 1)

    def test_connected_components(self):
        self.g.add_node(4)
        self.g.add_node(5)
        self.g.add_edge(4, 5, 6)
        self.g.add_edge(5, 4, 3)
        b = self.g2.connected_components()
        self.assertEqual(2, len(b))

    def test_plot_graph(self):
        self.g2.plot_graph()
