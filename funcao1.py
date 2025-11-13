#crie uma função que receba um nome como argumento (string) e retorne uma mensagem de saudação completa.
#resolução
def saudar(nome):
    return f"olá, {nome}! Seja bem-vindo!(a) ao mundo Python!"

#interação com o usuário
nome_usuario = input ("Digite seu nome: ")

#chamada da função e exibição do resultado
mensagem = saudar(nome_usuario)
print(mensagem)