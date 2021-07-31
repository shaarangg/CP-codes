def canConstruct(target, d):
    if target in d:
        return d[target]
    if target == "":
        return True
    for i in w:
        if target.startswith(i):
            suffix = target[len(i) :]
            if canConstruct(suffix, d):
                d[target] = True
                return True
    d[target] = False
    return False


target = input()
w = input().split()
print(canConstruct(target, {}))
