dataset = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0


def number_join(dataset):
    dataset = list(map(str, dataset))
    dataset.sort(key=cmp_to_key(xy_cmp))
    return "".join(dataset)

