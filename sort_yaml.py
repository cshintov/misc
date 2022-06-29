""" Sort yaml according to number of elements in list """
import yaml
from rich import print

servers = 'unsorted.yaml'
with open(servers, encoding="utf-8") as file:
    nodes = yaml.safe_load(file)

sorted_nodes = dict(
    sorted(nodes.items(), key=lambda item: len(item[1]))
)

print(sorted_nodes)

with open("sorted.yaml", mode="wt", encoding="utf-8") as file:
    yaml.dump(sorted_nodes, file, sort_keys=False)
