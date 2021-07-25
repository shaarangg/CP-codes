def countConstruct(target, d):
    if target in d:
        return d[target]
    if target == "":
        return 1
    totalCount = 0
    for i in a:
        if target.startswith(i):
            suffix = target[len(i) :]
            count = countConstruct(suffix, d)
            totalCount += count
    d[target] = totalCount
    return totalCount


s = input()
a = input().split()
print(countConstruct(s, {}))
