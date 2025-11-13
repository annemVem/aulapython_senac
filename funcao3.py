#crie uma função que receba o lado de um quandrado e retorne o valor da sua area ($A = Lado^2$)

def quadrado (lado):
    # usando o operador de exponenciação (**)
    return lado ** 2

#interação com o usuário
medida_lado = float(input("Digite a medida do lado do quadrado: "))

#chamada da função e exibição do resultado
area = quadrado(medida_lado)
print(f"A area do quadrado é: {area}")
