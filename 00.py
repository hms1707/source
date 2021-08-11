'''
f = open("C:/source/새파일.txt","w")
for i in range(1,11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
f.close()
'''
'''
f = open("C:/source/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
'''
'''
f = open("C:/source/새파일.txt","r")
while True:
        line = f.readline()
        if not line : break
        print(line, end='')
f.close()
'''
'''
while 1:
    data = input()
    if not data: break
    print(data)
'''
'''
f = open("C:/source/새파일.txt",'r')
lines = f.readlines()

print(type(lines))
print(lines)

for line in lines:         
            print(line,end='')
f.close()
'''
'''
f = open("C:/source/새파일.txt","r")
data = f.read()
print(data)
f.close
'''
'''
f = open("foo.txt", 'w')
f.write("Life is too shor. you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life in too short,tou need python")
'''
