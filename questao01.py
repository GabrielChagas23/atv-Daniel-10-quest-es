print("digite os três primeiros números em ordem crescente, o quarto não nescessariamente")
num1=int(input("digite um número: "))
num2=int(input("digite um segundo número: "))
num3=int(input("digite um terceiro número: "))
num4=int(input("digite um quarto número: "))

if num4 > num3:
    print(num4,'-',num3,'-',num2,'-',num1)
elif num3 > num4 > num2:
    print(num3,'-',num4,'-',num2,'-',num1)
elif num2 > num4 > num1:
    print(num3,'-',num2,'-',num4,'-',num1)
elif num1 > num4:
    print(num3,'-',num2,'-',num1,'-',num4)
