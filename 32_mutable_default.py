# https://florimond.dev/blog/articles/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
# https://frhyme.github.io/python-basic/default_parameter_value_in_python/

# Scoping Rule (LGB)
# 함수 내부 - Local Scope
# 전역 전역 - Global Scope
# 내장 영역 - Built-in Scopre

def foo():
    # global x    # 전역 변수 선언
    x = 10      # foo의 지역 변수
    print(x)    # foo의 지역 변수 출력
    print(locals())


foo()
# print(x)        # 에러. foo의 지역 변수는 출력할 수 없음
print("******************************")

#  클로저를 사용하면 프로그램의 흐름을 변수에 저장
#  클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용합


def calc():
    a = 3
    b = 5
    total = 0

    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(a, b, total)
        return total
    return mul_add


c = calc()
print(c(1), c(2), c(3), c(4), c(5))

print("******************************")

#  python의 default parameter는 가변적(mutable)

# def func1(a=[]) a가 함수 콜마다 []로 초기화되는 것이 아님
# 함수를 콜할 때마다 동일 object에 접근하게 됨
# parameter를 하나로서 관리하는 것은, recursion을 사용할 때 편리


def f(i, mylist):
    """파라미터 전달방식 - Mutable/Immutable"""
    i = i + 1
    mylist.append(0)


k = 10         # k는 int (immutable)
m = [1, 2, 3]  # m은 리스트 (mutable)
f(k, m)
print(k, m)
# 출력: 10 [1, 2, 3, 0]


def append(element, seq=[]):
    seq.append(element)
    return seq


print(append(1))
print(append(2))


def append(element, seq=None):  # =None 활용 !
    if seq is None:
        seq = []
    seq.append(element)
    return seq


print(append(1))
print(append(2))
