print("=== ANALISADOR DE SEGURANÇA DE SENHAS ===")

senha = input("Digite a senha para testar: ").strip()


tamanho_ok = len(senha) >= 8
tem_numero = False
tem_maiuscula = False
tem_minuscula = False
tem_caractere_especial = False

# Caracteres especiais considerados pelo programa
caracteres_especiais = "!@#$%^&*()-_=+[]{};:,.?/"


for caractere in senha:

    if caractere.isdigit():
        tem_numero = True

    if caractere.isupper():
        tem_maiuscula = True

    if caractere.islower():
        tem_minuscula = True

    if caractere in caracteres_especiais:
        tem_caractere_especial = True



print("\n=== RESULTADO DA ANÁLISE ===")

if tamanho_ok and tem_numero and tem_maiuscula and tem_minuscula and tem_caractere_especial:

    print("[+] Senha FORTE!")

else:

    print("[-] Senha FRACA. Critérios não atendidos:")

    if not tamanho_ok:
        print("    -> Deve ter pelo menos 8 caracteres.")

    if not tem_numero:
        print("    -> Deve conter pelo menos um número.")

    if not tem_maiuscula:
        print("    -> Deve conter pelo menos uma letra maiúscula.")

    if not tem_minuscula:
        print("    -> Deve conter pelo menos uma letra minúscula.")

    if not tem_caractere_especial:
        print("    -> Deve conter pelo menos um caractere especial.")

print("\nAnálise concluída.")
