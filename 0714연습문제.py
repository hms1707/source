#Q1
'''
def is_odd(a):
    if a%2 == 1:
        print('홀수')
    else:
        print('짝수')
'''

#Q2
'''
def avg_many(*a):
    return sum(a)/len(a)
'''

#Q3
'''
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
'''

#Q4
'''
3. print("you", "need", "python")
'''

#Q5
'''
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
'''

#Q6
'''
f = open("test.txt", 'a')
f.write(input(">>> "))
f.write('\n')
f.close()
'''

#Q7
'''
f1 = open("test1.txt", 'w')
f1.write("Life is too short\nyou need java")
f1.close()

f = open('test1.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test1.txt', 'w')
f.write(body)
f.close()
'''
