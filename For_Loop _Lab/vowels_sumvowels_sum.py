text = input()
a, e, i, o, u = 0, 0, 0, 0, 0

for ch in text:
    if ch == "a":
        a += 1
    elif ch == "e":
        e += 2
    elif ch == "i":
        i += 3
    elif ch == "o":
        o += 4
    elif ch == "u":
        u += 5

print(a + e + i + o + u)
