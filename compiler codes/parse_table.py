def calculate_first(grammar):
    first = {}
    for non_terminal in grammar:
        first[non_terminal] = set()
    while True:
        updated = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                # check if the symbol is terminal or non-terminal
                if production[0] not in grammar:
                    # check if this symbol isn't found in non-terminal list add it in first set
                    if production[0] not in first[non_terminal]:
                        first[non_terminal].add(production[0])
                        updated = True
                else:
                    for symbol in production:
                        if symbol not in first[non_terminal]:
                            first[non_terminal].update(first[symbol])
                            if 'epsilon' not in first[symbol]:
                                break
                            if symbol == production[-1]:
                                first[non_terminal].add('epsilon')
                                updated = True
        if not updated:
            break
    return first


def calculate_follow(grammar, first):
    follow = {}
    for non_terminal in grammar:
        follow[non_terminal] = set()
    start_symbol = list(grammar.keys())[0]
    follow[start_symbol].add('$')
    while True:
        updated = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                for i, symbol in enumerate(production):
                    if symbol in grammar:
                        rest = production[i+1:]
                        first_rest = set()
                        for s in rest:
                            if s in grammar:
                                first_s = first[s]
                                first_rest |= first_s - {'epsilon'}
                                if 'epsilon' not in first_s:
                                    break
                            else:
                                first_rest.add(s)
                                break
                        else:
                            first_rest |= follow[non_terminal]
                        if not follow[symbol].issuperset(first_rest):
                            follow[symbol] |= first_rest
                            updated = True
        if not updated:
            break
    return follow

def create_parse_table(grammar, first, follow):
    parse_table = {}
    for non_terminal, productions in grammar.items():
        parse_table[non_terminal] = {}
        for terminal in grammar[non_terminal]:
            if terminal != 'FOLLOW':
                parse_table[non_terminal][terminal] = []
        for production in productions:
            first_set = []
            for symbol in production:
                if symbol in grammar:
                    first_set += [x for x in first[symbol] if x != 'epsilon']
                    if 'epsilon' not in first[symbol]:
                        break
                else:
                    first_set.append(symbol)
                    break
            else:
                first_set += follow[non_terminal]
            for terminal in first_set:
                if terminal in parse_table[non_terminal]:
                    parse_table[non_terminal][terminal].append(production)
                else:
                    parse_table[non_terminal][terminal] = [production]
            if 'epsilon' in first_set:
                for terminal in follow[non_terminal]:
                    if terminal in parse_table[non_terminal]:
                        parse_table[non_terminal][terminal].append(production)
                    else:
                        parse_table[non_terminal][terminal] = [production]
    return parse_table


grammar = {
    'S': ['A B', 'C'],
    'A': ['A a', 'b'],
    'B': ['b'],
    'C': ['A C', 'd']
}
first = calculate_first(grammar)
follow = calculate_follow(grammar, first)
parse_table = create_parse_table(grammar, first, follow)

print('first set \n',first, '\n')
print('follow set \n',follow, '\n')
print('parse table \n',parse_table, '\n')