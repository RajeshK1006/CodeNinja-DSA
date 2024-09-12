def check(W, x, y, z):
    l = [x, y, z]
    l.sort()
    if W in l:
        return "YES"
    one = x + y
    two = y + z
    three = x + z
    four = x + y + z
    if W == one or W == two or W == three or W == four:
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    w, x, y, z = map(int, input().split())
    result = check(w, x, y, z)
    print(result)
