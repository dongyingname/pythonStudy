# %%
from math import pi
from collections import deque
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# %%
fruits.count('apple')
# %%
fruits.index('banana', 4)  # Find next banana starting a position 4
# %%
fruits.reverse()
fruits
# %%
fruits.append('grape')
fruits
# %%
fruits.sort()
fruits
# %%
fruits.pop()
# %%
# Use list as stack
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
# %%
stack.pop()
# %%
# Use list as queues
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()

# %%
# list comprehension
squares = []
for i in range(10):
    squares.append(i**2)
squares

# %%
squares = list(map(lambda x: x**2, range(10)))
squares
# %%
squares = [x**2 for x in range(10)]
squares

# %%
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# %%
# If the expression is a tuple (e.g. the (x, y) in the
# previous example), it must be parenthesized.
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[abs(x) for x in vec]

# %%
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# %%
[(x, x**2) for x in range(6)]

# %%
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]

# %%
[str(round(pi, i)) for i in range(1, 6)]

# %%
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# %%
[[row[i] for row in matrix] for i in range(4)]

# %%
for i in range(4):
    for row in matrix:
        print(row[i])

# %%
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

# %%
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
transposed

# %%
