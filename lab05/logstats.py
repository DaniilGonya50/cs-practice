def parse_event(line: str) -> dict:
    line = line.split(maxsplit=2)
    if len(line) != 3:
        raise ValueError
    if line[1] not in 'DEBUG INFO WARNING ERROR':
        raise ValueError
    data_line = {'time': line[0], 'level': line[1], 'message': line[2]}
    return data_line


def count_levels(lines: list[str]) -> dict:
    ...


def top_errors(lines: list[str], n: int) -> list[list]:
    ...


def format_report(counts: dict, errors: list[list]) -> str:
    ...
