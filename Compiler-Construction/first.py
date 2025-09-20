# 1. Simple Grammar with ε:
def compute_first(grammar, terminals, non_terminals):
    first = {nt: set() for nt in non_terminals}
    for t in terminals:
        first[t] = {t}
    
        epsilon = 'ε'
    
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
                    if symbol not in first:
                        continue
                    
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

grammar1 = {
    'S': [['A', 'B'], ['ε']],
    'A': [['a'], ['ε']],
    'B': [['b']]
}

terminals1 = {'a', 'b'}
non_terminals1 = {'S', 'A', 'B'}

first_sets1 = compute_first(grammar1, terminals1, non_terminals1)
print("FIRST Sets for Problem 1:")
for nt, fset in first_sets1.items():
    print(f"FIRST({nt}) = {fset}")


# 2. Left-Recursive Grammar:
def compute_first(grammar, terminals, non_terminals):
    first = {nt: set() for nt in non_terminals}
    for t in terminals:
        first[t] = {t}
    
        epsilon = 'ε'
    
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
                    if symbol not in first:
                        continue
                    
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

grammar2 = {
    'A': [['A', '+', 'id'], ['id']]
}

terminals2 = {'+', 'id'}
non_terminals2 = {'A'}

first_sets2 = compute_first(grammar2, terminals2, non_terminals2)
print("FIRST Sets for Problem 2:")
for nt, fset in first_sets2.items():
    print(f"FIRST({nt}) = {fset}")


# 3. Complex Grammar:
def compute_first(grammar, terminals, non_terminals):
    first = {nt: set() for nt in non_terminals}
    for t in terminals:
        first[t] = {t}
    
        epsilon = 'ε'
    
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
                    if symbol not in first:
                        continue
                    
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

grammar3 = {
    'Stmt': [['if', 'Expr', 'then', 'Stmt', 'ElsePart']],
    'ElsePart': [['else', 'Stmt'], ['ε']],
    'Expr': [['id']]
}

terminals3 = {'if', 'then', 'else', 'id'}
non_terminals3 = {'Stmt', 'ElsePart', 'Expr'}

first_sets3 = compute_first(grammar3, terminals3, non_terminals3)
print("FIRST Sets for Problem 3:")
for nt, fset in first_sets3.items():
    print(f"FIRST({nt}) = {fset}")

