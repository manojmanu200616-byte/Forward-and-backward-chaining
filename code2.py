# ---------- KNOWLEDGE BASE ----------
facts = {"A", "B"}

rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D")
]

# ---------- FORWARD CHAINING ----------
def forward_chaining(facts, rules):
    facts = set(facts)
    changed = True
    while changed:
        changed = False
        for cond, res in rules:
            if cond.issubset(facts) and res not in facts:
                facts.add(res)
                changed = True
    return facts


# ---------- BACKWARD CHAINING ----------
rule_dict = {
    "C": ["A", "B"],
    "D": ["C"]
}

def backward_chaining(goal, facts):
    if goal in facts:
        return True
    if goal not in rule_dict:
        return False
    for g in rule_dict[goal]:
        if not backward_chaining(g, facts):
            return False
    return True


# ---------- RESOLUTION ----------
def resolve(c1, c2):
    for lit in c1:
        if "-" + lit in c2:
            return (c1 | c2) - {lit, "-" + lit}
    return None


# ---------- RUN ----------
print("Forward Chaining Result:", forward_chaining(facts, rules))
print("Backward Chaining for D:", backward_chaining("D", facts))

clause1 = {"A", "B"}
clause2 = {"-A"}
print("Resolution Result:", resolve(clause1, clause2))
