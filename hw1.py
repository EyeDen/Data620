import networkx as nx

G = nx.Graph()

G.add_edge("Heather", "Ike")
G.add_edge("Ike", "Jane")

G.add_cycle(["Carol", "Fernando", "Heather", "Garth", "Ed", "Beverly", "Andre"])
G.add_cycle(["Andre", "Fernando", "Diane"])
G.add_cycle(["Diane", "Fernando", "Garth"])
G.add_cycle(["Garth", "Diane", "Beverly"])
G.add_cycle(["Beverly", "Andre", "Diane"])

G.add_edge("Carol", "Diane")
G.add_edge("Diane", "Ed")

nx.draw_networkx(G)