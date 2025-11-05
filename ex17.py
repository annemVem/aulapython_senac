'''
Uma loja de produtos tecnologicos te contratou para desenvolver um codigo da seguite forma:
(1)Leia um produto e de acordo com o produto verifique o preço. (Vide tabela abaixo)
(2)produtos-preço
mouse-10
teclado-20
memória-100
e (3)Leia ainda a quantidade de produtos comprados:
Calcule:
(4)total = preco * quantidade
(5)imposto = se a quantidade for maior que 10 calcule um imposto de  5% sobre o total  senaõ calcule 10% sobre o total
(6)valor final = total + imposto
'''
produto=input("Qual o produto?: ").upper()
if(produto == "MOUSE"):
    valor=10
elif(produto== "TECLADO"):
    valor=20
elif(produto== "MEMORIA"):
    valor=100
else:
    valor=0
    print("Produto não existe.")
qtd=int(input("Qual a quantidade?"))
total=valor*qtd
if (qtd>10):
    imposto=total*0.05
else:
    imposto=total*0.10
Valorfinal=total+imposto
print(f"O valor total do {produto} é:{Valorfinal} ")