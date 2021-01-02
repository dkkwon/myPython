# http://pythonstudy.xyz/python/article/16-%ED%95%A8%EC%88%98

def sum(a, b):  # 함수
    s = a + b
    return s


print(type(sum))

total = sum(4, 7)
print(total)


def f(i, mylist):  # 파라미터 전달방식 - Mutable/Immutable
    i = i + 1
    mylist.append(0)


k = 10       # k는 int (immutable)
m = [1, 2, 3]  # m은 리스트 (mutable)

f(k, m)      # 함수 호출
print(k, m)  # 호출자 값 체크
# 출력: 10 [1, 2, 3, 0]


def calc(i, j, factor=1):  # Default Parameter
    return i * j * factor


result = calc(10, 20)
print(result)


def report(name, age, score):  # Named Parameter
    print(name, score)


report(age=10, name="Kim", score=80)


def total(*numbers):  # 가변길이 파라미터
    tot = 0
    for n in numbers:
        tot += n
    return tot


t = total(1, 2)
print(t)
t = total(1, 5, 2, 6)
print(t)

def calc(*numbers): # return value
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot

count, sum = calc(1,5,2,6)  # (count, tot) 튜플을 리턴
print(count, sum)