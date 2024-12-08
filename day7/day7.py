from itertools import product

version1_ops = ['+', '*']
version2_ops = ['+', '*', '||']

def sum_results_of_operable(equations, operators_set):
    sum_results = 0
    for result, operands in equations:
        if check_operable(result, operands, operators_set):
            sum_results += result
    return sum_results

def check_operable(result, operands, operators_set):
    for operators in product(operators_set, repeat=len(operands)-1):
        try:
            total = operands[0]
            for op, operand in zip(operators, operands[1:]):
                if op == '+':
                    total += operand
                elif op == '*':
                    total *= operand
                elif op == '||':
                    total = int(str(total) + str(operand))
            if total == result:
                return True
        except:
            continue
    return False

def get_equations(input_data):
    equations = []
    for line_num, line in enumerate(input_data.strip().splitlines(), 1):
        if ": " not in line:
            print(f"Skipping invalid line {line_num}: '{line}'")
            continue
        result, ops = line.split(": ")
        operands = list(map(int, ops.split()))
        equations.append((int(result), operands))
    return equations

def read_input(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    test = read_input('./day7/test.txt')
    test_equations = get_equations(test)
    sum1 = sum_results_of_operable(test_equations, version1_ops)
    sum2 = sum_results_of_operable(test_equations, version2_ops)
    assert sum1 == 3749
    assert sum2 == 11387
    
    data = read_input('./day7/day7.txt')
    equations = get_equations(data)
    
    sum1 = sum_results_of_operable(equations, version1_ops)
    sum2 = sum_results_of_operable(equations, version2_ops)
    print(f"\nSum of Operable Results (using '+' and '*'): {sum1}")
    print(f"Sum of Operable Results after adding '||': {sum2}")

if __name__ == "__main__":
    main()