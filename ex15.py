ano=int(input("Qual ano do seu nascimento?"))
genero=input("Qual seu genero (M/F?)?").upper()
idade= 2025-ano
if(idade>= 18 and genero == "M"):
  print("Você está apto")
elif (genero=="F"):
  print(F"você tem  {idade} anos. Canditado genero feminino, sem alistamento.")
else:
  print(f"você tem  {idade} anos. Não está apto")