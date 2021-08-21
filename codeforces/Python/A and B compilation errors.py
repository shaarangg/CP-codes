n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
da = {}
db = {}
dc = {}
for i in a:
    if da.get(i, 0) == 0:
        da[i] = 1
    else:
        da[i] = da[i] + 1
for i in b:
    if db.get(i, 0) == 0:
        db[i] = 1
    else:
        db[i] = db[i] + 1
for i in c:
    if dc.get(i, 0) == 0:
        dc[i] = 1
    else:
        dc[i] = dc[i] + 1
for key in da:
    if da.get(key, 0) != db.get(key, 0):
        print(key)
for key in db:
    if db.get(key, 0) != dc.get(key, 0):
        print(key)
