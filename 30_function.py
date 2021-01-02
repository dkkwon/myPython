
# def 함수이름():
#      코드

def sum(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""  # docstring
    s = a + b
    return s


print(type(sum))
total = sum(4, 7)
print(total)


def sample():
    """pass - do nothing"""
    pass


print(sample.__doc__)
# pass - do nothing

help(sample)
# Help on function sample in module __main__:
# sample()
#     pass - do nothing


def calc(*numbers):
    """return value - (count, tot) 튜플을 리턴"""
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot


count, sum = calc(1, 5, 2, 6)
print(count, sum)
