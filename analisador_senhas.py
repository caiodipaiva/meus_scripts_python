print("=== ANALISADOR DE SEGURANÇA DE SENHAS ===")

senha = input("Digite a senha para testar: ")

# Variáveis para checar os critérios de segurança
tem_numero = False
tem_maiuscula = False
tamanho_ok = len(senha) >= 8

# O laço FOR passa por cada letra da senha para analisar
for caractere in senha:
    if caractere.isdigit(): # Verifica se é um número
        tem_numero = True
    if caractere.isupper(): # Verifica se é uma letra maiúscula
        tem_maiuscula = True

# A estrutura IF/ELSE decide se a senha é segura ou não
if tamanho_ok and tem_numero and tem_maiuscula:
    print("\n[+] Resultado: Senha FORTE! Boa escolha.")
else:
    print("\n[-] Resultado: Senha FRACA. Motivos:")
    if not tamanho_ok:
        print("    -> Deve ter pelo menos 8 caracteres.")
    if not tem_numero:
        print("    -> Deve conter pelo menos um número.")
    if not tem_maiuscula:
        print("    -> Deve conter pelo menos uma letra maiúscula.")
