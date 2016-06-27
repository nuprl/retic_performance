

def convert_to_set(res):
    res_tuple=set()
    for r in res:
        (e1, e2, w) = r
        res_tuple.add((e1, e2))
    return res_tuple


print(convert_to_set([(1, 2, 3)]))
