#Crie uma função que receba dois numeros e retorne o maior deles.
def numero (num1, num2):
    if num1 > num2:
        return f"O {num1} é maior!"
    elif num2 > num1:
        return f"O {num2} é maior!"
    else:
        return "Os dois numeros são iguais! "
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(numero(n1, n2))