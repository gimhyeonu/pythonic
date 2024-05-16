from random import *

j = 0

for i in range(1, 51):
    customer = randint(5,50)
    if 5 <= customer <= 15 :
        print("[O] {0}번째 손님 (소요시간 : {1})".format(i,customer))
        j += 1
    elif customer > 15 :
        print(("[ ] {0}번째 손님 (소요시간 : {1})".format(i,customer)))
    
print(f"총 탑승 승객: {j} 분")