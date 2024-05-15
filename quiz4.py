from random import *

lst = range(1, 21)
lst = list(lst)

shuffle(lst)

print(""" -- 당첨자 발표 --
치킨 당첨자 :""",lst[0], """
커피 당첨자 :""", sample(lst[1:20], 3),"""
 -- 축하합니다 --- """)