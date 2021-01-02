# 최대 재귀 깊이(maximum recursion depth)가 1,000

def hello():
    print('Hello, world!')
    hello()

# hello()
# 테스트 시 997번 찍었네?


def hello(count):
    if count == 0:  # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return

    print('Hello, world!', count)

    count -= 1
    hello(count)    # with no return vallue

hello(5)    # hello 함수 호출


def make_seqlist(element, seq=[]):
    if element == 0:
        return seq

    seq.append(element)
    element -= 1
    # return make_seqlist(element)
    return make_seqlist(element, seq)   # with return vallue

# seq = []
# print(make_seqlist(3, seq))
print(make_seqlist(3))

# make_seqlist(3)   # NameError: name 'seq' is not defined
# print(seq)
