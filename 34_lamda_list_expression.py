# https://dojang.io/mod/page/view.php?id=2360

# lambda expression (anonymous function)
g = lambda x: x + 10
print(g)
print(g(1))

print((lambda x: x + 10)(1))

# (lambda x: y = 10; x + y)(1)
# SyntaxError: invalid syntax

# map(함수, 반복가능객체)
# filter(함수, 반복가능객체)
# reduece(함수, 반복가능객체)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lambda x: str(x) if x % 3 == 0 else x, a)
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(filter(lambda x: x > 5 and x < 10, b)))
print(list(filter(lambda x: x < 5 or x > 10, b)))

from functools import reduce
c = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, c))

# list expression
print([str(x) for x in a if x % 3 == 0])
print([x for x in a if x > 5 and x < 10])
