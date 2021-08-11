#add
'''
f=open("c:\source\새파일.txt","a")
for i in range(11,20):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()
'''

#with
'''
with open("foo.txt","w") as f:
    f.write("Life is too short, you need python")
'''

