def count_by_extension(paths):
    result = {}
    for path in paths:
        suf_ind = path.rfind('.')
        if suf_ind == 0 or suf_ind == -1:
        #     continue
        # elif suf_ind == -1:
            result[''] = result.get('', 0) + 1
        else:
            result[path[suf_ind + 1:].lower()] = result.get(path[suf_ind + 1:], 0) + 1
    return result


def deepest_path(paths):
    if paths == []:
        return ''
    deepest = ''
    for path in paths:
        if path.count('/') > deepest.count('/') or (path.count('/') == deepest.count('/') and path < deepest):
            deepest = path
    return deepest


def human_size(n_bytes):
    if n_bytes < 1024:
        return f'{n_bytes} Б'
    n_bytes /= 1024
    k = 1
    while n_bytes > 1024:
        n_bytes /= 1024
        k += 1
    if k == 1:
        return f'{n_bytes:.1f} КБ'
    elif k == 2:
        return f'{n_bytes:.1f} МБ'
    elif k == 3:
        return f'{n_bytes:.1f} ГБ'
    else:
        return f'{n_bytes:.1f} ТБ'


paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
print(count_by_extension(paths))
print(deepest_path(paths))
print(human_size(900))
print(human_size(1536))
print(human_size(5 * 1024 * 1024))
