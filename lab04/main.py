from stats import average_by_city, read_valid, warmest_city
import sys


lines = sys.stdin.read().splitlines()
valid_lines = read_valid(lines)
best_city = warmest_city(valid_lines)
best_temp = average_by_city(valid_lines)[best_city]
print(len(valid_lines))
print(len(lines) - len(valid_lines))
print(best_temp)
