'''
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
  print(first + last)
'''

'''
number = 0
for mark in kors:
  number += 1
  if mark >= 60:
    print("%d번 학생은 합격입니다."%number)
  else:
    print("%d번 학생은 불합격입니다."%number)
'''

'''
#조건1] 한 과목이라도 40점 미만이면 불합격
#조건2] 세 과목의 평균이 60점 이상 합격

sws = [60,65,55,70,65]
dbs = [55,60,65,65,70]
oss = [60,75,60,70,60]


for number in range(len(sws)):
  sw = sws[number]
  db = dbs[number]
  os = oss[number]

  total = sw + db + os
  ave = total / 3

      # 조건 1                        #조건 2
  if sw < 40 or db < 40 or os < 40 or ave < 60 :
    print("%d학생은 불합격입니다." % (number + 1))
  else:
    print("%d학생은 합격입니다." % (number + 1))

'''

'''
add = 0
for i in range(1,11):
  add += i
print(add)
'''

for i in range(2,10):
  for j in range(1, 10):
     print(i*j, end="     ")
  print('')






















