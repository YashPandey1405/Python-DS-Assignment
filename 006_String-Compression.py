# Write a code to perform basic string compression using the counts of repeated characters

name = "yyyzzzzbbaaaaaaacccccccdddff"
ans = ""
n = len(name)
idx = 0

while idx < n:
    ch = name[idx]
    count = 1
    while idx + 1 < n and ch == name[idx + 1]:
        idx += 1
        count += 1
    ans += ch + str(count)
    idx += 1

print(ans)
