def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True
    while changed:
        changed = False
        for premise, conclusion in rules:
            if set(premise).issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                changed = True
    return inferred

def backward_chaining(goal, facts, rules):
    if goal in facts:
        return True
    for premise, conclusion in rules:
        if conclusion == goal:
            return all(backward_chaining(p, facts, rules) for p in premise)
    return False

def resolution(clause1, clause2):
    return list(set(clause1) | set(clause2))

def main():
    facts = ['A']
    rules = [(['A'], 'B'), (['B'], 'C')]
    print("Forward:", forward_chaining(facts, rules))
    print("Backward:", backward_chaining('C', facts, rules))
    print("Resolution:", resolution(['A'], ['~A','B']))

main()
