def count_by_extension(paths):
    result = {}
    for path in paths:
        suf_ind = path.rfind('.')
        if suf_ind == 0 or suf_ind == -1:
            continue
        result[path[suf_ind + 1:]] = result.get(path[suf_ind + 1:], 0) + 1
    return result


def deepest_path(paths):
    ...


def human_size(n_bytes):
    ...


paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
print(count_by_extension(paths))
