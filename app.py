import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

palavraSecreta = input("Digite a palavra secreta: ").upper()

tentativas = []
palavraSecretaList = list(palavraSecreta)
palavraSecretaCheck = []
palavraSecretaCheck = ['_'] * len(palavraSecretaList)
tentativasnum = 8
preliminar = ""

print(palavraSecretaList)

for i, letra in enumerate(palavraSecretaCheck) :
    print (preliminar + palavraSecretaCheck[i], end=" ")

while (tentativasnum > 1) :
    print(" ")
    letraTentada = input("Digite o palpite de letra: ").upper()
    tentativas.append(letraTentada)

    if letraTentada in palavraSecretaList :
        for i, letra in enumerate(palavraSecretaList) :
            if letra == letraTentada :
                palavraSecretaCheck[i] = letraTentada
                correto = 1
                clear()


        if '_' not in palavraSecretaCheck:
            print("Parabéns!, a palavra secreta era", palavraSecreta)
            break
    
    if letraTentada not in palavraSecretaList :
        tentativasnum = tentativasnum - 1   
        print (palavraSecretaCheck)
        correto = 0
        clear()

    for i, letra in enumerate(palavraSecretaCheck) :
        print (preliminar + palavraSecretaCheck[i], end=" ")

    if (correto == 1) :
        print(" ")
        print("Letra correta!")

    if (correto == 0) :
        print (" ")
        print("Letra incorreta.")

    print(" ")
    print("Restam ", tentativasnum, " tentativas")

    
if '_' in palavraSecretaCheck:
    print("Suas tentativas acabaram, tente novamente.")
    
