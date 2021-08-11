'''
a = [1,2,3]

try:
    print(a[3])
    4/0
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
'''

try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
