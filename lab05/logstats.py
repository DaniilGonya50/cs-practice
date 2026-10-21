def parse_event(line: str) -> dict:
    line = line.split(maxsplit=2)
    if len(line) != 3:
        raise ValueError
    if line[1] not in 'DEBUG INFO WARNING ERROR':
        raise ValueError
    data_line = {'time': line[0], 'level': line[1], 'message': line[2]}
    return data_line


def count_levels(lines: list[str]) -> dict:
    data_levels = {}
    for line in lines:
        data_levels[line['level']] = data_levels.get(line['level'], 0) + 1
    return data_levels


def top_errors(lines: list[str], n: int) -> list[list]:
    messages_count = {}
    for line in lines:
        if line['level'] != 'ERROR':
            continue
        messages_count[line['message']] = messages_count.get(line['message'], 0) + 1
    messages_count = [list(x) for x in messages_count.items()]
    messages_count = sorted(messages_count, key=lambda x: (-x[1], x[0]))
    return messages_count[:n]

    


def format_report(counts: dict, errors: list[list]) -> str:
    ...
