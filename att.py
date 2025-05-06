import random
numero_secreto = random.randint(1, 100)
print("Tente adivinhar o numero entre 1 e 100!")
tentativas = 0
while True:
    tentativa = int(input("Digite sua tentativa: "))
    tentativas += 1
    if tentativa < numero_secreto:
        print("O numero é MAIOR que isso.")
    elif tentativa > numero_secreto:
        print("O numero é MENOR que isso.")
    else:
        print(f"Parabens! Voce acertou o numero em {tentativas} tentativas.")
        break
