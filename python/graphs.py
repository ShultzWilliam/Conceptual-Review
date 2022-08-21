#Code to explore the concepts fo graphs and non-linear data structures
#Start date: April 19th, 2022

#A node class to define the nodes within a graph.
class node:
    def __init__(self, value : str = "none") -> None:
        self.value = value
        self.links = []

    def __repr__(self) -> str:
        return self.value

    def info(self):
        return self.value

    def connections(self):
        return self.links

    def rename(self, newValue: str):
        self.value = newValue

#A graph class consisting of several nodes linked together to one another
class graph:
    def __init__(self, name):
        self.name = name
        self.nodes = []

    def insertNode(node: node):
        pass

    def deleteNode(node: node):
        pass
        

a = node("Moon")
print(a.info())
print(a.connections())

b = node("Earth")
print(b)

a.links.insert(0,b)
b.links.insert(0,a)

print(f"Moon branches: {a.connections()}")
print(f"Earth branches: {b.connections()}")

c = graph("SolarSystem")
