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

    
