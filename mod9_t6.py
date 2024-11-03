def all_variants(text):
    n = len(text)
    for x in range(n):
        for y in range(x+1, n+1):
            yield text[x:y]


a = all_variants("abс")
for i in a:
    print(i)
