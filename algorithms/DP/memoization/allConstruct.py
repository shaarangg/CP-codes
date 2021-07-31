def append(j, i):
    j.insert(0, i)
    return j


def allConstruct(target, d):
    if target in d:
        return d[target]
    if target == "":
        return [[]]
    result = []
    for i in a:
        if target.startswith(i):
            suffix = target[len(i) :]
            suffixList = allConstruct(suffix, d)
            targetList = list(map(lambda j: append(j, i), suffixList))
            result += targetList
    d[target] = result
    return result


s = input()
a = input().split()
print(allConstruct(s, {}))
