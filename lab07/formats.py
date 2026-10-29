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


print(csv_to_records("id,город\n1 ,Азов\n2 ,Шахты"))
