# if <condition> :
# for <var> in range() :
# while <condition> :
# local operator -> and, or, not

# 단축평가: 순차적 조건 확인 ('and', 'or' 는 단축평가 보장)

# x = int(input())
x = 71
if x == 10 or x == 111:
    print("x == 10 or x == 111")
elif 70 <= x < 80:
    print("70 <= x < 80")
elif x >= 80 and x < 90:
    print("x >= 80 and x < 90")
else:
    print('Hello', 'world', sep=' ')
    print('Hello', 'world', sep='x')

y = x if x == 10 else 0
print('y=', y)
print("******************************")

# False
bool(0)
bool(0.0)
bool(())
bool([])
bool({})
bool(None)

# for loop: str, tuple, list, dictionary, iterator, generator
for i in range(3):
    print('hello(', i, ')')

for i in range(8, 10):
    print('hello(', i, ')')
print('')

# 20 <= i < 50
for i in range(20, 50, 10):
    print('hello(', i, ')')

print("******************************")
rangelist = [2009, 10, 11]
print(rangelist)

for i in rangelist:
    print('hello(', i, ')')

for index, i in enumerate(rangelist):
    print('index:', index, ', hello(', i, ')')

for index in range(len(rangelist)):
    print('index:', index, ', hello(', rangelist[index], ')')

print(list(range(1, -3, -1)))
print("******************************")

a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}
print(a)
print(b)
print(a & b)
