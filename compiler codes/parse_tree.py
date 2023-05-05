# import operator

# OPERATORS = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv,
# }
# LEFT_PAREN = "("
# RIGHT_PAREN = ")"


# def build_parse_tree(expression):
#     tree = {}
#     stack = [tree]
#     node = tree
#     for token in expression:
#         if token == LEFT_PAREN:
#             node["left"] = {}
#             stack.append(node)
#             node = node["left"]
#         elif token == RIGHT_PAREN:
#             node = stack.pop()
#         elif token in OPERATORS:
#             node["val"] = token
#             node["right"] = {}
#             stack.append(node)
#             node = node["right"]
#         else:
#             node["val"] = int(token)
#             parent = stack.pop()
#             node = parent
#     return tree


# def print_parse_tree(tree, level=0):
#     if "val" in tree:
#         print(" " * level + str(tree["val"]))
#         print_parse_tree(tree["left"], level + 2)
#         print_parse_tree(tree["right"], level + 2)
#     else:
#         for child in tree.values():
#             print_parse_tree(child, level)


# ex = "(3*5+(2+7)-6)"
# parse_tree = build_parse_tree(ex)
# print_parse_tree(parse_tree)

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
