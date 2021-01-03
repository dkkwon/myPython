# List Comprehension (리스트 내장) - [출력표현식 for 요소 in 입력Sequence [if 조건식]]
oldlist = [1, 2, 'A', False, 3]
newlist = [i*i for i in oldlist if type(i) == int]
print(newlist) # [1, 4, 9]
print("******************************")


# Set Comprehension
oldlist = [1, 1, 2, 3, 3, 4]
newlist = {i*i for i in oldlist}
print(newlist) # {16, 1, 9, 4}
print("******************************")


# Dictionary Comprehension - {Key:Value for 요소 in 입력Sequence [if 조건식]}
id_name = {1: '박진수', 2: '가만진', 3: '홍수정'}
name_id = {val: key for key, val in id_name.items()}
print(name_id) # {'박진수': 1, '가만진': 2, '홍수정': 3}


def isodd(val): return val % 3


mydict = {x: isodd(x) for x in range(10)}
print(mydict) # {0: 0, 1: 1, 2: 2, 3: 0, 4: 1, 5: 2, 6: 0, 7: 1, 8: 2, 9: 0}
print("******************************")


# Generator Comprehension (Generator Expression)
g = (n*n for n in range(5))
# print(type(g))  # <class 'generator'>

# 리스트로 일괄 변환시
# mylist = list(g)

for i in range(3):
    value = next(g)
    print('-', value)

# 나머지 모두 출력
for x in g:
    print(x)
