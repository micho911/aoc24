import re

def read_input(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def extract_multiplications(line):
    return [(int(x), int(y)) for x, y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)]

def parse_multiplications(lines):
    return [
        pair 
        for line in lines 
        for pair in extract_multiplications(line)
    ]

def parse_enabled_multiplications(input_string):
    cleaned_string = re.sub(r"don't\(\).*?do\(\)", "", input_string)
    return extract_multiplications(cleaned_string)

def calculate_multiplication_sum(multiplications):
    return sum(x * y for x, y in multiplications)

def main():
    test1 = read_input('./day3/test1.txt')
    res1 = parse_multiplications(test1)
    assert calculate_multiplication_sum(res1) == 161

    test2 = read_input('./day3/test2.txt')
    input_string = ''.join(test2)
    res2 = parse_enabled_multiplications(input_string)
    assert calculate_multiplication_sum(res2) == 48

    # Main input processing
    day3 = read_input('./day3/day3.txt')
    res1 = parse_multiplications(day3)
    print(f"First calculation result: {calculate_multiplication_sum(res1)}")

    singled = ''.join(day3)
    res2 = parse_enabled_multiplications(singled)
    print(f"Second calculation result: {calculate_multiplication_sum(res2)}")

if __name__ == "__main__":
    main()