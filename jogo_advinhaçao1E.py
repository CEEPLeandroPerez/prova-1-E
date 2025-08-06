print("Leandro Hilebrand Perez")
print("prova de introduçao a programaçao")

import random
import os

erros = 0
sorteado = random.randrange(0, 100)
jogador = int(input("Digite seu número!"))

while sorteado != jogador:
    os.system('cls')  # Limpa a tela
    if sorteado > jogador:
        print("ERRO, o número é maior")
    elif sorteado < jogador:
        print("ERRO, o número é menor")
    erros += 1  # Conta a tentativa errada
    jogador = int(input("Digite seu número:"))

print(f"Você acertou o número {sorteado} em {erros + 1} tentativas.")