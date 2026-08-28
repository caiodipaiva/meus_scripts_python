#Dicionario com os autorizados a entrar no sistema.
usuarios = {
    "michelle" : 456,
    "caio" : 555
}

print("=== Sistema de Controle de Acesso ===")

#Aqui eu dou ao usuario 3 tentativas de acesso.
tentativas = 3

#Começo o loop.
for i in range(tentativas):
    
    #Ultilizo o (\n) para pular uma linha. # .lower() evita problemas com maiúsculas
    chegaram = input("\nInsira seu nome: ").lower().strip() #Evita problemas com espaços.
    
    # Validação para o programa não quebrar se o usuário digitar letras na senha
    senha_input = input("Insira sua senha: ")
    if not senha_input.isdigit(): #.isdigit serve pra confirmar que é um numero.
        print("A senha deve conter apenas números!")
        continue
    cracha = int(senha_input)
    
    if chegaram in usuarios and cracha == usuarios[chegaram]:
        print(f"Bem vindo, {chegaram}! Acesso liberado.")
        break
    else:
        # Mensagem genérica para segurança (Impede enumeração de usuários)
        print(f"Dados incorretos! Tentativas restantes: {tentativas - 1 - i}")
else:
    # Esse else só roda se o usuário errar todas as 3 vezes
    print("\n🚨 ACESSO BLOQUEADO: Número de tentativas esgotadas!")
