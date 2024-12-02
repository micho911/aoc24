# day 2 of advent of code 2024

def read_input():
    reports = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            reports.append(list(map(int, line.split())))
        except EOFError:
            break
    return reports

def is_safe(report):
    if report == sorted(report):
        return all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    elif report == sorted(report, reverse=True):
        return all(-3 <= report[i+1] - report[i] <= -1 for i in range(len(report) - 1))
    return False

def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe(report))

def count_safe_reports_dampened(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
        else:
            for i in range(len(report)):
                dampened_report = report[:i] + report[i+1:]  # Remove one level
                if is_safe(dampened_report):
                    count += 1
                    break
    return count

def main():
    reports = read_input()
    print(count_safe_reports(reports))
    print(count_safe_reports_dampened(reports))

if __name__ == "__main__":
    main()