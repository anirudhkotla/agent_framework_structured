import networkx as nx


class MemoryGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_relation(self, source, relation, target):
        self.graph.add_node(source)
        self.graph.add_node(target)
        self.graph.add_edge(source, target, relation=relation)

    def get_relations(self):
        data = []

        for u, v, d in self.graph.edges(data=True):
            data.append({
                "source": u,
                "relation": d["relation"],
                "target": v
            })

        return data


memory_graph = MemoryGraph()