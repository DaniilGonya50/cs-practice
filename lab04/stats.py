def parse_record(line: str) -> dict:
    if len(line.split(';')) != 3:
        raise ValueError('Передано не три поля')
    city, temp, date = line.split(';')
    if city == '' or date == '':
        raise ValueError('Поля город или дата пустые')
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError('Температура не число')
    total = {'city': city, 'temp': temp, 'date': date}
    return total


def read_valid(lines: list[str]) -> list[dict]:
    a = []
    for line in lines:
        try:
            d = parse_record(line)
            a.append(d)
        except ValueError:
            continue
    return a


def average_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    mid_temps = {}
    for record in records:
        city, temp, date = record.values()
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
    for city in total:
        mid_temps[city] = f'{(total[city] / count[city]):.1f}'
    return mid_temps
