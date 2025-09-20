# ------------------ FIRST FUNCTION ------------------
def compute_first(grammar, terminals, non_terminals, epsilon='ε'):
    first = {nt: set() for nt in non_terminals}
    for t in terminals:
        first[t] = {t}
    
    changed = True
    while changed:
        changed = False
        for nt in non_terminals:
            for production in grammar[nt]:
                if production == [epsilon]:
                    if epsilon not in first[nt]:
                        first[nt].add(epsilon)
                        changed = True
                    continue
                
                all_epsilon = True
                for symbol in production:
                    new_symbols = first[symbol] - {epsilon}
                    if new_symbols - first[nt]:
                        first[nt].update(new_symbols)
                        changed = True
                    if epsilon not in first[symbol]:
                        all_epsilon = False
                        break
                
                if all_epsilon:
                    if epsilon not in first[nt]:
                        first[nt].add(epsilon)
                        changed = True
    
    first = {k: v for k, v in first.items() if k in non_terminals}
    return first

# ------------------ FOLLOW FUNCTION ------------------
def compute_follow(grammar, start_symbol, first, terminals, non_terminals, epsilon='ε', end_marker='$'):
    follow = {nt: set() for nt in non_terminals}
    follow[start_symbol].add(end_marker)
    
    changed = True
    while changed:
        changed = False
        for nt in non_terminals:
            for production in grammar[nt]:
                for i, symbol in enumerate(production):
                    if symbol not in non_terminals:
                        continue
                    
                    trailer = production[i+1:]
                    
                    trailer_first = set()
                    if trailer:
                        for t_symbol in trailer:
                            if t_symbol in terminals:
                                trailer_first.add(t_symbol)
                                break
                            trailer_first.update(first[t_symbol] - {epsilon})
                            if epsilon not in first[t_symbol]:
                                break
                        else:
                            trailer_first.add(epsilon)
                    else:
                        trailer_first.add(epsilon)
                    
                    # Add FIRST(trailer) - epsilon
                    new_symbols = trailer_first - {epsilon} - follow[symbol]
                    if new_symbols:
                        follow[symbol].update(new_symbols)
                        changed = True
                    
                    # If trailer can be epsilon, add FOLLOW of LHS
                    if epsilon in trailer_first:
                        new_symbols = follow[nt] - follow[symbol]
                        if new_symbols:
                            follow[symbol].update(new_symbols)
                            changed = True
    return follow

# ------------------ TEST GRAMMARS ------------------

# 1. Basic Grammar
grammar1 = {'S': [['A', 'B']], 'A': [['a'], ['ε']], 'B': [['b'], ['ε']]}
terminals1 = {'a', 'b'}
non_terminals1 = {'S', 'A', 'B'}
start1 = 'S'

first1 = compute_first(grammar1, terminals1, non_terminals1)
follow1 = compute_follow(grammar1, start1, first1, terminals1, non_terminals1)
print("1. Basic Grammar FOLLOW:", follow1)

# 2. Grammar with Recursion
grammar2 = {'E': [['E', '+', 'T'], ['T']], 'T': [['id']]}
terminals2 = {'+', 'id'}
non_terminals2 = {'E', 'T'}
start2 = 'E'

first2 = compute_first(grammar2, terminals2, non_terminals2)
follow2 = compute_follow(grammar2, start2, first2, terminals2, non_terminals2)
print("2. Recursive Grammar FOLLOW:", follow2)

# 3. If-Else Grammar
grammar3 = {'S': [['if', 'E', 'then', 'S', 'Else']], 'Else': [['else', 'S'], ['ε']], 'E': [['id']]}
terminals3 = {'if', 'then', 'else', 'id'}
non_terminals3 = {'S', 'Else', 'E'}
start3 = 'S'

first3 = compute_first(grammar3, terminals3, non_terminals3)
follow3 = compute_follow(grammar3, start3, first3, terminals3, non_terminals3)
print("3. If-Else Grammar FOLLOW:", follow3)
