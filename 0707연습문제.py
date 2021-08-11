#Q1
'''
a= "Life is too short, you need python"

if "wife" in a: print("wife")   #출력x
elif "python" in a and "you" not in a: print("python")  #출력x
elif "shirt" not in a: print("shirt")   #출력o, 이후로 출력x
elif "need" in a: print("need")
else: print("none")
'''
# "shirt"가 출력된다.

#Q2
'''
a=0
i=0
while a<=1000:
        a+=1        # 누적연산 ( x += y )
        b=a%3
        if b == 0:
            i += a
print(i)
'''
#Q3
'''
a=0
while a < 5:
    a=a+1
    b="*"*a
    print(b)
'''
#Q4
'''
for i in range(1,101):
    print(i)
'''
#Q5
'''
a = [70,60,55,75,95,90,80,80,85,100]
for i in a:
    b += i
print(b/len(a))
'''
#Q6
'''
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
        
print (result)

numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n % 2 == 1]

print (result)
'''






