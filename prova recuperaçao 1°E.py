import random
import string

def password_generator(Len_pass=8):
    # Definir as opções possíveis para a senha
    ascii_options = string.ascii_letters  # Letras maiúsculas e minúsculas
    number_options = string.digits        # Dígitos
    punt_options = string.punctuation     # Caracteres especiais
    options = ascii_options + number_options + punt_options

    # Inicializa a senha gerada
    password_user = ""

    # Gera a senha com o número de dígitos especificado
    for i in range(Len_pass):
        digit = random.choice(options)
        password_user += digit

    return password_user

# Solicitar ao usuário o número de caracteres para a senha
choice_user = input("Quantos dígitos na senha? ")

# Verificar se a entrada é um número válido
if choice_user.isdigit():
    choice_user = int(choice_user)
    # Gerar e mostrar a senha
    generated_password = password_generator(Len_pass=choice_user)
    print(f"Sua senha gerada é: {generated_password}")
else:
    print("Entrada inválida.")
