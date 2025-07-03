s = "abca"
seen = set()
for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)
