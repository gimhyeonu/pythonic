from random import *

print(random()) # 0.0 ~ 1.0 미만
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10) + 1) # 1 ~ 10 이하

print(int(random() * 45) + 1) # 1 ~ 45 이하

print(randrange(1,46)) # 1 ~ 46 미만

print(randint(1, 45))