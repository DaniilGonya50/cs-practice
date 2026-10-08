def parse_record(line):
    if len(line.split(';')) != 3:
        raise ValueError('Передано не три поля')
    city, temp, date = line.split(';')
    if city == '' or date == '':
        raise ValueError('Поля город или дата пустые')
    if city != city.strip() or temp != temp.strip() or date != date.strip():
        raise ValueError('Лишние пробелы')
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError('Температура не число')
    total = {'city': city, 'temperature': temp, 'date': date}
    return total


def read_valid(lines):
    valid_lines = []
    for line in lines:
        try:
            d = parse_record(line)
            valid_lines.append(d)
        except ValueError:
            continue
    return valid_lines


def average_by_city(records):
    total = {}
    count = {}
    mid_temps = {}
    for record in records:
        city, temp, date = record.values()
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
    for city in total:
        mid_temps[city] = float(f'{(total[city] / count[city]):.1f}')
    return mid_temps


def warmest_city(records):
    mid_temps = average_by_city(records)
    best = ''
    for city in mid_temps:
        if best == '' or mid_temps[city] > mid_temps[best] or (mid_temps[city] == mid_temps[best] and city < best):
            best = city
    return best
