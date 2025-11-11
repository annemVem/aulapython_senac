senha_correta = "123456"
tentativas = 0
max_tentativas = 3
while tentativas < max_tentativas:
    tentativa=input(f"Digite a senha (Tentativa {tentativas +1} / {max_tentativas})")
    if tentativa == senha_correta:
        print("Acesso concedido! Bem vindo. ")
        break
    else:
        print("Senha incorreta")
        tentativas+=1
else:
    print("Você excedeu o número max de tentativa. Acesso bloqueado")