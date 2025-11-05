nota1=float(input("Digite sua nota 1: "))
nota2=float(input("Digite sua nota 2: "))
nota3=float(input("Digite sua nota 3: "))
media=(nota1+nota2+nota3)/3
print("A média da sua nota é: ", media)
if(media>=7):
    print(f"Você está aprovado, sua média é: {media}")
else:
    print (f"Você etá reprovado, sua média é: {media}")