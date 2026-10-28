def count_by_extension(paths):
    result = {}
    for path in paths:
        suf_ind = path.rfind('.')
        if suf_ind == 0:
            continue
        elif suf_ind == -1:
            result[''] = result.get('', 0) + 1
        else:
            result[path[suf_ind + 1:].lower()] = result.get(path[suf_ind + 1:], 0) + 1
    return result


def deepest_path(paths):
    ...


def human_size(n_bytes):
    ...


paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
print(count_by_extension(paths))
