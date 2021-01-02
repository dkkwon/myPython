# Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
# https://dojang.io/mod/page/view.php?id=2345

def print_numbers(a, b, c):
    """positional argument"""
    print(a)
    print(b)
    print(c)


print_numbers(10, 20, 30)
x = [40, 50, 60]

# list unpacking
print_numbers(*x)
print_numbers(*[41, 51, 61])
print("******************************")


def print_numbers3(a, *args):
    print(a)
    print(args)


print_numbers3(1, 10, 20)


def calc(i, j, factor=1):
    """Default Parameter"""
    return i * j * factor


result = calc(10, 20)
print(result)


def report(name, age, score):
    """Named Parameter"""
    print(name, age, score)


report(age=10, name="Kim", score=80)
print(10, 20, 30, sep=':', end='')
print("******************************")


def personal_info(name, age, address):
    """Default Parameter"""
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(*x)   # unpacking key
personal_info(**x)  # unpacking value
print("******************************")

# personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
# personal_info(**{'name': '홍길동', 'age': 30})


def personal_info(**kwargs):
    """keyword arguments"""
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
        print(kw, ': ', arg)
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])


y = {'name': '길동', 'age': 3, 'address': '용산구 이촌동'}
personal_info(**y)


def custom_print(*args, **kwargs):
    print(*args, **kwargs)


custom_print(1, 2, 3, sep=':', end='\n')
print("******************************")
