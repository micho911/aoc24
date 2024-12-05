
def read_input(filename):
    with open(filename, 'r') as file:
        return file.read()

def check_valid_update(rules, update):
    return all(
        not any(successor in update[:i] for successor in rules.get(str(number), []))
        for i, number in enumerate(update)
    )

def get_valid_updates(rules, updates):
    return [update for update in updates if check_valid_update(rules, update)]

def get_middle_number(updates):
    return sum(x[len(x) // 2] for x in updates)

def get_invalid_updates(rules, updates):
    valid_updates = get_valid_updates(rules, updates)
    return [x for x in updates if x not in valid_updates]

def resolve_order(update, rules):
    graph = {num: set() for num in update}
    for num in update:
        str_num = str(num)
        if str_num in rules:
            graph[num] = {x for x in update if x in rules[str_num]}
    
    visited = set()
    stack = []
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for pred in graph[node]:
            dfs(pred)
        stack.append(node)
    
    for num in update:
        dfs(num)
    
    return stack[::-1]

def make_right_order_for_invalid_updates(rules, updates):
    return [resolve_order(update, rules)[::-1] for update in updates]

def get_rules_and_updates(lines):
    rule_lines, update_lines = lines.split('\n\n')
    
    rules = {}
    for line in rule_lines.splitlines():
        number, successor = line.split('|')
        rules.setdefault(number, []).append(int(successor))
    
    updates = [list(map(int, line.split(','))) for line in update_lines.splitlines()]
    
    return rules, updates

def main():
    test1 = read_input('./day5/test.txt')
    rules, updates = get_rules_and_updates(test1)
    
    assert get_middle_number(get_valid_updates(rules, updates)) == 143
    
    invalid_updates = get_invalid_updates(rules, updates)
    corrected_updates = make_right_order_for_invalid_updates(rules, invalid_updates)
    
    assert get_middle_number(corrected_updates) == 123
    
    day5 = read_input('./day5/day5.txt')
    rules, updates = get_rules_and_updates(day5)
    
    print(get_middle_number(get_valid_updates(rules, updates)))

    assert get_middle_number(get_valid_updates(rules, updates)) == 4959

    print(get_middle_number(make_right_order_for_invalid_updates(rules, get_invalid_updates(rules, updates))))

if __name__ == "__main__":
    main()