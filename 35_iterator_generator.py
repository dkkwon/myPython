# print(dir([1,2,3]))

# iterator object (반복): str, tuple, list, range, set, dict
# sequence object (순서): str, tuple, list, range

# 제너레이터: __next__ 메서드를 호출 --> 함수 안의 yield까지 코드를 실행 후 yield generate 하여 리턴

it = [1, 2, 3].__iter__()
print(it.__next__())
print(it.__next__())

hellow = 'Hello, World!'
it = iter(hellow)
print(it.__next__())
print(it.__next__())
print(it.__next__())

it = iter(range(3))
print(it.__next__())
print(it.__next__())
print(it.__next__())

# k = [1, 2, 3]
k = 'Hel'
a, b, _ = k   # unpacking
print(a, b)
print("******************************")


def number_generator():
    yield 'K'
    yield 'W'
    yield 'O'
    yield 'N'

print(dir(number_generator))

for i in number_generator():
    print(i)

g = number_generator()
print(g)
# print(dir(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


def one_generator():
    yield 'one_generator'
    return 'return value'

print(one_generator())
try:
    g = one_generator()
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)    # return value

def upper_generator(x):
    for i in x:
        yield i.upper()    # 함수의 반환값을 바깥으로 전달

fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)