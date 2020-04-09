"""
このファイルに解答コードを書いてください
"""
a = input()
a = int(a)

if a%3==0 and a%5==0:
    print(a,":FizzBuzz")
elif a%3==0 :
    print(a,":Fizz")

elif a%5==0:
    print(a,":Buzz")
else:
    print("")