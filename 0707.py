#구구단
'''
for i in range(2,10):
  for j in range(1, 10):
    print(i, "*", j, "=", i*j, end=" ")
  print('')
'''
'''
for i in range(2,10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j:<4}', end=" ")
    print('')
'''
#리스트 내포
'''
a=['one', 'two','hi', '^^;']

result = []

for num in a :
  result.append(num)
print(result)
'''

'''
a=[1,2,3,4]
result = []

for num in a :
  if num % 2 == 0:
   result.append(num*3)
print(result)
'''

'''
a=[1,2,3,4]
result = [num*3 for num in a if num % 2 == 0]

print(result)

'''


#함수 정의
'''
def add_many(*args):    #args는 튜플의 형태로 저장한다.
    result=0
    print(args)
    for i in args:
        result += i
    return result
'''
'''
def add_mul(choice, *args):
    if choice =="add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    else:
        print("'add' 또는 'mul'을 선택하세요.")
    return result
'''
'''
def add_and_mul(a,b):
    return a+b, a*b
'''
'''
def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
'''


#vartest
'''
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)
'''

#lambda
'''
>>> add = lambda a, b: a+b
>>> result = add(3, 4)
>>> print(result)
7
'''


#파일 읽고 쓰기
'''
f=open("C:/source/새파일.txt",'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''














