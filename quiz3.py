# site = "http://naver.com"
site = "http://google.com"


main = site[7:site.find(".")]
three = main[0:3]
count = len(main)
e_count = main.count("e")

print(f"생성된 비밀번호 : {three}{count}{e_count}!")

