s={10, 20, 30}
s.add(40)
print(s)
print(set([1, 2, 3, 3, 4, 4]))
print({1, 2, 3} & {2, 3, 4})   # intersection {2, 3}
print({1, 2} | {2, 3})         # union {1, 2, 3}
print({1, 2, 3} - {2})        # difference {1, 3}