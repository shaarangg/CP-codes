m = list(map(int, input().split()))
w = list(map(int, input().split()))
x = [500, 1000, 1500, 2000, 2500]
hs, hu = map(int, input().split())
ts = 0
for i in range(5):
    ts += max(0.3 * x[i], ((1 - (m[i] / 250)) * x[i] - 50 * w[i]))
ts += hs * 100 - hu * 50
print(int(ts))
