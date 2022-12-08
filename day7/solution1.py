"""
Day 7 puzzle 1
"""

from __future__ import annotations
from typing import Optional, List


class Node:
    """
    A class to represent file system items
    """
    def __init__(
        self,
        node_name: str,
        node_type: str,
        node_parent: Optional[Node] = None,  # the root node has no parent!
        node_size: int = 0  # folders do not have size
    ) -> None:
        self.name = node_name
        self.type = node_type
        self.parent = node_parent
        self.size = node_size
        self.path = self.get_path()

    def __repr__(self):
        representation = (
            f'Node(name={self.name}, '
            + f'type={self.type}, '
            + f'size={self.size}, '
            + f'parent={self.parent})'
        )
        return representation

    def get_path(self):
        parents = [self.name]
        parent = self.parent
        while parent is not None:
            parents.append(parent.name)
            parent = parent.parent
        return "".join(list(reversed(parents)))


def parse_script(script: List[str]) -> dict[str: Node]:
    """
    A function to parse the input script. It detect cd and ls commands and
    builds the data structure.
    """

    i: int = 0
    wd: Node = None
    nodes: dict[str: Node] = {}
    while i < len(script):
        line = script[i]

        if line.startswith("$") and "cd" in line:
            # we're moving in a new node
            new_node_name = line.split(" ")[-1]
            if new_node_name == "..":
                wd = wd.parent
            else:
                node = Node(new_node_name, "dir", wd)
                node_path = node.get_path()
                nodes[node_path] = node
                wd = node
            i += 1

        elif line.startswith("$") and "ls" in line:
            # we need to parse next lines
            j = i + 1
            ls_line = script[j]
            while "$" not in ls_line:
                ls = ls_line.split(" ")
                if ls[0] == "dir":
                    node = Node(ls[1], "dir", wd)
                else:
                    node = Node(ls[1], "file", wd, int(ls[0]))
                node_path = node.get_path()
                nodes[node_path] = node
                j += 1
                if j >= len(script):
                    break
                ls_line = script[j]
            i = j

        else:
            raise ValueError(f"Invalid command: {' '.join(line)}")

    return nodes


def main(path: str) -> int:
    """
    Solution to day 7 puzzle 1
    """

    with open(path, encoding="utf-8") as fin:
        script = [line.strip() for line in fin]

    nodes: dict[str: Node] = parse_script(script)

    for node in filter(lambda node: node.type == "file", nodes.values()):
        parent = node.parent
        while parent is not None:
            parent.size += node.size
            parent = parent.parent

    res = sum(
        map(
            lambda node: node.size,
            filter(
                lambda node: node.size < 100000 and node.type == "dir",
                nodes.values()
            )
        ))
    print(res)
    return res


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
