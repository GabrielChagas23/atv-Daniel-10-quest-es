print("Digite três números em ordem crescente, e um quarto que não siga essa regra")

n1 = int(input("digite um número: "))
n2 = int(input("digite um segundo número: "))
n3 = int(input("digite um terceiro número: "))
n4 = int(input("digite um quarto número: "))


if n4 > n3:
    print(n4,n3,n2,n1)
elif n3 > n4 > n2:
    print(n3,n4,n2,n1)
elif n2 > n4 > n1:
    print(n3,n2,n4,n1)
elif n1 > n4:
    print(n3,n2,n1,n4)
    