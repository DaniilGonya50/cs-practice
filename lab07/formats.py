import json

def csv_to_records(text):
    lines = text.strip().splitlines()
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(',')]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(',')]
        record = {}
        for i, h in enumerate(headers):
            record[h] = values[i] if i < len(values) else ''
        records.append(record)
    return records


def cast_value(value):
    v = value.strip()
    if v == '':
        return v
    if v.lower() in ('true', 'yes'):
        return True
    if v.lower() in ('false', 'no'):
        return False
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    return v


def parse_settings(lines):
    result = {}
    current_list_key = None
    for line in lines:
        if '#' in line:
            line = line[:line.index('#')]
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('- '):
            item = stripped[2:].strip()
            if current_list_key is not None:
                result[current_list_key].append(cast_value(item))
            continue
        if ':' in stripped:
            colon_pos = stripped.index(':')
            key = stripped[:colon_pos].strip()
            value_part = stripped[colon_pos + 1:].strip()
            if value_part == '':
                result[key] = []
                current_list_key = key
            else:
                current_list_key = None
                result[key] = cast_value(value_part)
        else:
            pass
    return result


print(parse_settings(["# отчёт", "title: Отчёт за март", "decimals: 1", "active: true", "columns:", "  - город", "  - цена"]))
