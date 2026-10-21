from logstats import parse_event, count_levels, top_errors, format_report
import sys


path = sys.stdin.readline().strip()
n = 3
lines = []
with open(path, encoding='utf-8') as log:
    for line in log:
        lines.append(line)

counts = count_levels(lines)
errors = top_errors(lines, n)
report = format_report(counts, errors)

total = sum(counts.values())
error_count = counts.get('ERROR', 0)
broken_count = counts.get('BROKEN', 0)
print(total)
print(error_count)
print(broken_count)
with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
