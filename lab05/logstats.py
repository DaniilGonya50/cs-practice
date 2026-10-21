def parse_event(line: str) -> dict:
    line = line.split(maxsplit=2)
    if len(line) != 3:
        raise ValueError
    if line[1] not in 'DEBUG INFO WARNING ERROR':
        raise ValueError
    if line[0] == '' or line[1] == '' or line[2] == '':
        raise ValueError
    data_line = {'time': line[0], 'level': line[1], 'message': line[2]}
    return data_line


def count_levels(lines: list[str]) -> dict:
    data_levels = {}
    for line in lines:
        if line.strip() == '':
            continue
        try:
            parsed = parse_event(line)
            level = parsed['level']
            data_levels[level] = data_levels.get(level, 0) + 1
        except (ValueError, KeyError):
            data_levels['BROKEN'] = data_levels.get('BROKEN', 0) + 1
    return data_levels


def top_errors(lines: list[str], n: int) -> list[list]:
    messages_count = {}
    for line in lines:
        try:
            parsed = parse_event(line)
        except (ValueError, KeyError):
            continue
        if parsed['level'] != 'ERROR':
            continue
        msg = parsed['message']
        messages_count[msg] = messages_count.get(msg, 0) + 1
    result = sorted(messages_count.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, count] for msg, count in result[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ['Отчёт по журналу', '']
    for level in sorted(counts.keys()):
        lines.append(f'{level}: {counts[level]}')
    lines.append('')
    lines.append('Частые ошибки:')
    for error in errors:
        lines.append(f'- {error[0].strip()} — {error[1]}')
    return '\n'.join(lines) + '\n'
