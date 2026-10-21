from logstats import parse_event, count_levels, top_errors, format_report


path = input('Введите имя файла: ')
n = int(input('Введите количество самых частых ошибок для вывода в отчет: '))
lines = []
with open(path, encoding='utf-8') as log:
    for line in log:
        if line == '':
            continue
        try:
            lines.append(parse_event(line))
        except:
            lines.append({'time': 0, 'level': 'BROKEN', 'message': ''})
counts = count_levels(lines)
errors = top_errors(lines, n)
report = format_report(counts, errors)
with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
