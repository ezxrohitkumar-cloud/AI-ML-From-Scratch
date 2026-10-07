square = lambda x: x * 2 if False else x ** 2
print(square(4))   
words = ["banana", "fig", "apple"]
print(sorted(words, key=lambda w: len(w)))        # ['fig', 'apple', 'banana']
print(list(map(lambda x: x * 2, [1, 2, 3])))      # [2, 4, 6]
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # [2, 4]