from typing import NamedTuple


class Node(NamedTuple):
    parent: str
    name: str

def get_input():
    with open('input.txt', 'r') as f:
        data = f.read()
    return data

def compute(data):
    nodes = {'COM': Node('', 'COM')}
    for line in data.strip().splitlines():
        parent, name = line.split(')')
        nodes[name] = Node(parent, name)

    count = 0
    for node in nodes.values():
        while node.name != 'COM':
            count += 1
            node = nodes[node.parent]
    return count

print(compute(get_input()))
