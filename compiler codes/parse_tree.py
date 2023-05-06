from lark import Lark, Tree

grammar = """
    start: expr
    expr: atom | expr "+" atom
    atom: NUMBER | "(" expr ")"
    %import common.NUMBER
    %import common.WS
    %ignore WS
"""


def print_tree(tree, level=0):
    print("  " * level + tree.data)
    for child in tree.children:
        if isinstance(child, Tree):
            print_tree(child, level=level + 1)
        else:
            print("  " * (level + 1) + child)


parser = Lark(grammar)

input_str = "3 + (4 + 5)"

parse_tree = parser.parse(input_str)

print_tree(parse_tree)
