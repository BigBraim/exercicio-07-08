import random
print('')
def main():

    numero_minimo = 1
    numero_maximo = 5


    numero_sorteado = random.randint(numero_minimo, numero_maximo)

    print("Bem-vindo ao sorteio de números!")
    print(f"O número sorteado está entre {numero_minimo} e {numero_maximo}.")


    tentativas = 0
    while True:
        tentativa = int(input("Tente adivinhar o número: "))
        tentativas += 1

        if tentativa < numero_sorteado:
            print("Tente um número maior.")
        elif tentativa > numero_sorteado:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativas} tentativas.")
            break
main()
