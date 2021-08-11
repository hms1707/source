f=open("C:/source/새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line,end='')
f.close()
